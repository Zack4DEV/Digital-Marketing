import streamlit as st

# Shared Tailwind CSS classes
bg_card = "bg-card rounded-lg p-4"
text_primary = "text-primary"
input_field = "input-field"
border_b = "border-b border-border"
py_2 = "py-2"

def create_new_campaign():
    st.write('<div class="mb-4">')
    st.write(f'<div class="{bg_card}">')
    st.write('<h2 class="text-lg font-bold mb-2">Create New Campaign</h2>')
    st.write(f'<input type="text" placeholder="Campaign Name" class="{input_field}" />')
    st.write(f'<textarea placeholder="Description" rows="3" class="{input_field}"></textarea>')
    st.write(f'<input type="text" placeholder="Target Audience" class="{input_field}" />')
    st.write('<button class="bg-primary text-primary-foreground py-2 px-4 rounded-lg mt-2">Create Campaign</button>')
    st.write('</div>')
    st.write('</div>')

def active_campaigns():
    st.write('<div>')
    st.write(f'<div class="{bg_card}">')
    st.write('<h2 class="text-lg font-bold mb-2">Active Campaigns</h2>')
    st.write('<table class="w-full table-fixed">')
    st.write('<thead>')
    st.write('<tr>')
    st.write('<th class="text-left">Name</th>')
    st.write('<th class="text-left">Status</th>')
    st.write('<th class="text-right">Reach</th>')
    st.write('<th class="text-right">Engagement</th>')
    st.write('</tr>')
    st.write('</thead>')
    st.write('<tbody>')
    st.write('<tr>')
    st.write(f'<td class="{border_b} {py_2}">Summer Collection</td>')
    st.write(f'<td class="{border_b} {py_2}">Active</td>')
    st.write(f'<td class="{border_b} text-right {py_2}">50K</td>')
    st.write(f'<td class="{border_b} text-right {py_2}">4.8%</td>')
    st.write('</tr>')
    st.write('<tr>')
    st.write(f'<td class="{border_b} {py_2}">Fitness Challenge</td>')
    st.write(f'<td class="{border_b} {py_2}">Active</td>')
    st.write(f'<td class="{border_b} text-right {py_2}">30K</td>')
    st.write(f'<td class="{border_b} text-right {py_2}">3.2%</td>')
    st.write('</tr>')
    st.write('<tr>')
    st.write(f'<td class="{border_b} {py_2}">Tech Reviews</td>')
    st.write(f'<td class="{border_b} {py_2}">Planned</td>')
    st.write(f'<td class="{border_b} text-right {py_2}">0</td>')
    st.write(f'<td class="{border_b} text-right {py_2}">0%</td>')
    st.write('</tr>')
    st.write('</tbody>')
    st.write('</table>')
    st.write('</div>')
    st.write('</div>')

st.markdown('<div class="bg-background text-primary-foreground min-h-screen p-4">', unsafe_allow_html=True)
create_new_campaign()
active_campaigns()
st.markdown('</div>', unsafe_allow_html=True)
