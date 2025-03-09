import streamlit as st
import sqlite3
import pandas as pd
import os

class DatabaseClient:
    """
    A client for interacting with a SQLite database.
    """

    def __init__(self, db_url="marketing_platform.db", migrate=False, migration_scripts_path="migrations"):
        """
        Initializes the DatabaseClient with the specified database URL and migration options.

        Args:
            db_url (str): The URL or path to the SQLite database file.
            migrate (bool): Whether to run database migrations.
            migration_scripts_path (str): The path to the directory containing migration scripts.
        """
        self.db_url = db_url
        self.migrate = migrate
        self.migration_scripts_path = migration_scripts_path
        self.conn = None

        if self.migrate:
            self.run_migrations()

    def connect(self):
        """
        Connects to the SQLite database.
        """
        try:
            self.conn = sqlite3.connect(self.db_url)
        except sqlite3.Error as e:
            st.error(f"Database connection error: {e}")

    def disconnect(self):
        """
        Disconnects from the SQLite database.
        """
        if self.conn:
            self.conn.close()
            self.conn = None

    def execute_query(self, query, params=None):
        """
        Executes a SQL query and returns the results as a Pandas DataFrame.

        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): Parameters to pass to the query.

        Returns:
            pandas.DataFrame: The query results as a DataFrame, or None if an error occurs.
        """
        try:
            if not self.conn:
                self.connect()

            if params:
                df = pd.read_sql_query(query, self.conn, params=params)
            else:
                df = pd.read_sql_query(query, self.conn)

            return df
        except sqlite3.Error as e:
            st.error(f"Database query error: {e}")
            return None
        finally:
            self.disconnect()

    def execute_insert(self, query, params=None):
        """
        Executes an INSERT query.

        Args:
            query (str): The SQL INSERT query to execute.
            params (tuple, optional): Parameters to pass to the query.
        """
        try:
            if not self.conn:
                self.connect()

            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            st.error(f"Database INSERT error: {e}")
        finally:
            self.disconnect()

    def create_table(self, query):
        """
        Executes a table creation query.

        Args:
            query (str): The SQL create table query to execute.
        """
        try:
            if not self.conn:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            st.error(f"Database table creation error: {e}")
        finally:
            self.disconnect()

    def run_migrations(self):
        """
        Runs database migrations from the specified directory.
        """
        if not os.path.exists(self.migration_scripts_path):
            st.warning(f"Migration scripts directory not found: {self.migration_scripts_path}")
            return

        migration_files = sorted([f for f in os.listdir(self.migration_scripts_path) if f.endswith(".sql")])

        for file in migration_files:
            migration_path = os.path.join(self.migration_scripts_path, file)
            try:
                with open(migration_path, "r") as f:
                    migration_sql = f.read()
                if not self.conn:
                    self.connect()
                cursor = self.conn.cursor()
                cursor.executescript(migration_sql)
                self.conn.commit()
                st.success(f"Migration {file} applied successfully.")
            except sqlite3.Error as e:
                st.error(f"Migration error in {file}: {e}")
            finally:
                self.disconnect()