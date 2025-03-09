import streamlit as st
import pandas as pd
import plotly.express as px
import random
from auth import check_authentication, get_user_id
from common.db_client import DatabaseClient

# Initialize the database client
db_client = DatabaseClient()

def campaign_insights_page():
    """Displays the Campaign Insights page with database integration."""

    if not check_authentication():
        st.warning("Please log in to access this page.")
        return

    st.title("Campaign Insights & Performance Dashboard")

    st.markdown("""
    <p>Dive deep into your campaign performance with our advanced analytics dashboard. Visualize key metrics, identify trends, and optimize your strategies for maximum ROI.</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    user_id = get_user_id()

    # Fetch campaigns for the logged-in user
    campaigns_query = "SELECT id, name FROM campaigns WHERE user_id = ?"
    campaigns_df = db_client.execute_query(campaigns_query, (user_id,))

    if campaigns_df is None or campaigns_df.empty:
        st.warning("No campaigns found for this user. Please create a campaign first.")
        return

    campaign_id = st.selectbox("Select Campaign", campaigns_df['name'].tolist(), index=0)
    selected_campaign_id = campaigns_df[campaigns_df['name'] == campaign_id]['id'].iloc[0]

    # Fetch campaign insights for the selected campaign
    insights_query = "SELECT * FROM campaign_insights WHERE campaign_id = ?"
    insights_df = db_client.execute_query(insights_query, (selected_campaign_id,))

    if insights_df is None or insights_df.empty:
        st.warning("No insights found for the selected campaign.")
        return

    # Key Metrics
    st.subheader("Key Performance Indicators (KPIs)")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Impressions", insights_df['impressions'].sum())
    col2.metric("Total Clicks", insights_df['clicks'].sum())
    col3.metric("Total Conversions", insights_df['conversions'].sum())
    col4.metric("Total Spend", f"${insights_df['spend'].sum():.2f}")

    st.markdown("---")

    # Campaign Performance Overview
    st.subheader("Campaign Performance Overview")

    # Bar Chart: Clicks vs. Impressions
    st.markdown("<h5>Clicks vs. Impressions</h5>", unsafe_allow_html=True)
    fig_clicks_impressions = px.bar(insights_df, x='date', y=['clicks', 'impressions'], barmode='group', title='Clicks and Impressions by Date')
    st.plotly_chart(fig_clicks_impressions)

    # Line Chart: Conversions Over Campaigns
    st.markdown("<h5>Conversions Over Time</h5>", unsafe_allow_html=True)
    fig_conversions = px.line(insights_df, x='date', y='conversions', title='Conversions Per Date')
    st.plotly_chart(fig_conversions)

    # Scatter Plot: Spend vs. Conversions
    st.markdown("<h5>Spend vs. Conversions</h5>", unsafe_allow_html=True)
    fig_spend_conversions = px.scatter(insights_df, x='spend', y='conversions', title='Spend vs. Conversions')
    st.plotly_chart(fig_spend_conversions)

    st.markdown("---")

    # Advanced Analytics
    st.subheader("Advanced Analytics & Segmentation")
    st.markdown("""
    <p>Segment your audience and analyze performance by demographic, location, or other custom dimensions to refine your targeting.</p>
    """, unsafe_allow_html=True)

    # Placeholder for advanced features (replace with actual logic)
    st.write("Coming Soon: Advanced segmentation and custom analytics.")

    st.markdown("---")

    # Real-Time Reporting
    st.subheader("Real-Time Reporting & Insights")
    st.markdown("""
    <p>Monitor campaign performance in real-time and make data-driven decisions on the fly. Stay ahead of the competition with up-to-the-minute insights.</p>
    """, unsafe_allow_html=True)

    # Placeholder for real-time data (replace with actual logic)
    st.write("Real-time data feeds and live dashboards are coming soon.")

if __name__ == "__main__":
    campaign_insights_page()