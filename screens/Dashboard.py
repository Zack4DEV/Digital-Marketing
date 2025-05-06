import streamlit as st

# Shared Tailwind CSS classes
BG_BACKGROUND = "bg-background"
TEXT_PRIMARY_FOREGROUND = "text-primary-foreground"
MIN_H_SCREEN = "min-h-screen"
P_4 = "p-4"
MB_4 = "mb-4"
ROUNDED_LG = "rounded-lg"
W_FULL = "w-full"
BG_CARD = "bg-card"
TEXT_LG = "text-lg"
FONT_BOLD = "font-bold"
FLEX = "flex"
FLEX_ROW = "flex-row"
JUSTIFY_BETWEEN = "justify-between"
W_1_2 = "w-1/2"
MR_2 = "mr-2"
ML_2 = "ml-2"

def campaign_performance_component():
    st.markdown('<div class="{} {} {} {}">'.format(BG_BACKGROUND, TEXT_PRIMARY_FOREGROUND, MIN_H_SCREEN, P_4), unsafe_allow_html=True)
    
    st.markdown('<div class="{}">'.format(MB_4))
    st.image("https://placehold.co/400x200/DDDDDD/FFFFFF?text=AI+Assistant", caption="AI Assistant", output_format="JPEG", use_column_width=True)
    st.markdown('</div>')
    
    st.markdown('<div class="{} {} {}">'.format(BG_CARD, ROUNDED_LG, P_4))
    st.markdown('<h2 class="{} {} {}">'.format(TEXT_LG, FONT_BOLD, MB_2), "Campaign Performance")
    st.markdown('<div class="{} {} {}">'.format(BG_CARD, ROUNDED_LG, P_4))
    st.image("https://placehold.co/300x220/DDDDDD/FFFFFF?text=Chart", caption="Campaign Performance Chart", output_format="JPEG", use_column_width=True)
    st.markdown('</div>')
    st.markdown('</div>')
    
    st.markdown('<div class="{} {}">'.format(FLEX, FLEX_ROW))
    st.markdown('<div class="{} {}">'.format(W_1_2, MR_2))
    st.markdown('<div class="{} {} {}">'.format(BG_CARD, ROUNDED_LG, P_4))
    st.markdown('<h2 class="{} {} {}">'.format(TEXT_LG, FONT_BOLD, MB_2), "Engagement Rate")
    st.markdown("4.8%")
    st.markdown('</div>')
    st.markdown('</div>')
    
    st.markdown('<div class="{} {}">'.format(W_1_2, ML_2))
    st.markdown('<div class="{} {} {}">'.format(BG_CARD, ROUNDED_LG, P_4))
    st.markdown('<h2 class="{} {} {}">'.format(TEXT_LG, FONT_BOLD, MB_2), "Reach")
    st.markdown("50.2K")
    st.markdown('</div>')
    st.markdown('</div>')
    st.markdown('</div>')
    
    st.markdown('<div class="{} {}">'.format(BG_CARD, ROUNDED_LG, P_4))
    st.markdown('<h2 class="{} {} {}">'.format(TEXT_LG, FONT_BOLD, MB_2), "Active Campaigns")
    st.markdown('<ul>')
    st.markdown('<li>Summer Collection Launch</li>')
    st.markdown('<li>Fitness Challenge</li>')
    st.markdown('<li>Tech Review Series</li>')
    st.markdown('</ul>')
    st.markdown('</div>')

campaign_performance_component()
