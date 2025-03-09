-- migrations/001_create_users_table.sql

-- Create the users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL, -- Add password hash for security
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create the campaigns table
CREATE TABLE IF NOT EXISTS campaigns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    name TEXT NOT NULL,
    start_date DATE,
    end_date DATE,
    budget REAL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create the campaign_insights table
CREATE TABLE IF NOT EXISTS campaign_insights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    campaign_id INTEGER,
    date DATE,
    impressions INTEGER,
    clicks INTEGER,
    conversions INTEGER,
    spend REAL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
);

-- Create the data_analysis table (for storing analysis results or metadata)
CREATE TABLE IF NOT EXISTS data_analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    file_name TEXT,
    analysis_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    analysis_results TEXT, -- Store results as JSON or text
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create the features table (for storing feature usage or settings)
CREATE TABLE IF NOT EXISTS features (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    feature_name TEXT NOT NULL,
    usage_count INTEGER DEFAULT 0,
    last_used DATETIME,
    settings TEXT, -- Store feature settings as JSON or text
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);