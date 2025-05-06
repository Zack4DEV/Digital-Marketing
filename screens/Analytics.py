import streamlit as st

# Shared Tailwind CSS classes
CARD_STYLE = "bg-card p-4 rounded-lg"
TEXT_PRIMARY = "text-primary"
TEXT_PRIMARY_FOREGROUND = "text-primary-foreground"
IMG_STYLE = "w-full h-48"

def render_card(title, img_src, alt_text):
    st.markdown(f'<div class="{CARD_STYLE}">', unsafe_allow_html=True)
    st.markdown(f'<h2 class="{TEXT_PRIMARY} text-lg mb-2">{title}</h2>', unsafe_allow_html=True)
    st.image(img_src, alt=alt_text, output_format='JPEG', width=None, use_column_width='always')
    st.markdown('</div>', unsafe_allow_html=True)

def render_metrics_card(title, metrics):
    st.markdown(f'<div class="{CARD_STYLE}">', unsafe_allow_html=True)
    st.markdown(f'<h2 class="{TEXT_PRIMARY} text-lg mb-2">{title}</h2>', unsafe_allow_html=True)
    for metric in metrics:
        st.markdown(f'<p class="{TEXT_PRIMARY_FOREGROUND}">{metric}</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    st.markdown('<div class="bg-background text-primary-foreground min-h-screen p-4">', unsafe_allow_html=True)

    render_card("Weekly Engagement", "https://openui.fly.dev/openui/400x220.svg?text=Weekly+Engagement", "Weekly Engagement Chart")

    render_card("Audience Age Distribution", "https://openui.fly.dev/openui/400x220.svg?text=Audience+Age+Distribution", "Audience Age Distribution Chart")

    render_card("Platform Distribution", "https://openui.fly.dev/openui/400x220.svg?text=Platform+Distribution", "Platform Distribution Chart")

    render_metrics_card("Key Metrics", [
        "Total Followers: 125K",
        "Average Engagement Rate: 4.8%",
        "Content Performance Score: 8.5/10"
    ])

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
