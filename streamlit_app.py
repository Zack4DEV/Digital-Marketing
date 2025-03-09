
import streamlit as st

# Set the page configuration for the Streamlit app
st.set_page_config(
    page_title="Digital Marketing ",
)

# Shared Tailwind CSS classes
TW_CONTAINER = "container mx-auto"
TW_TEXT_CENTER = "text-center"
TW_TEXT_LG = "text-lg"
TW_TEXT_XL = "text-xl"
TW_TEXT_2XL = "text-2xl"
TW_TEXT_GRAY = "text-gray-700"
TW_TEXT_BLUE = "text-blue-500"
TW_TEXT_WHITE = "text-white"
TW_BG_BLUE = "bg-blue-500"
TW_BG_WHITE = "bg-white"
TW_BORDER = "border"
TW_ROUNDED = "rounded"
TW_PX_4 = "px-4"
TW_PY_2 = "py-2"
TW_MY_4 = "my-4"
TW_W_FULL = "w-full"
TW_H_FULL = "h-full"
TW_RELATIVE = "relative"
TW_OVERFLOW_Y_AUTO = "overflow-y-auto"

def marketing_expert_component():
    st.markdown('<div class="bg-background text-primary-foreground p-8 flex flex-col items-center justify-center">', unsafe_allow_html=True)
    st.markdown('<h1 class="text-4xl font-bold mb-4">Become A Marketing Expert</h1>', unsafe_allow_html=True)
    st.markdown('<p class="text-center mb-6 text-lg">Unlock Your Full Potential With Expert Guidance</p>', unsafe_allow_html=True)

    st.markdown('<div class="{GRID_CLASSES}">', unsafe_allow_html=True)
    st.markdown('<button class="bg-primary text-primary-foreground {BUTTON_CLASSES}">Get Started</button>', unsafe_allow_html=True)
    st.markdown('<button class="bg-primary text-primary-foreground {BUTTON_CLASSES}">Learn More</button>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<p class="{TEXT_CENTER_CLASSES} {TEXT_CLASSES}">Inspiring Creativity One Idea At A Time</p>', unsafe_allow_html=True)
    st.markdown('<p class="text-center mb-6">Transforming Creators into Storytelling Masters</p>', unsafe_allow_html=True)

    st.markdown('<div class="{GRID_CLASSES}">', unsafe_allow_html=True)
    st.markdown('<button class="bg-secondary text-secondary-foreground {BUTTON_CLASSES}">Learn More</button>', unsafe_allow_html=True)
    st.markdown('<button class="bg-secondary text-secondary-foreground {BUTTON_CLASSES}">Monthly Membership</button>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<p class="text-center mt-6">Let\'s Build Your Digital Marketing Empire Now</p>', unsafe_allow_html=True)

    st.markdown('<div class="{GRID_CLASSES}">', unsafe_allow_html=True)
    st.markdown('<button class="bg-accent text-accent-foreground {BUTTON_CLASSES}">Join Now</button>', unsafe_allow_html=True)
    st.markdown('<button class="bg-accent text-accent-foreground {BUTTON_CLASSES}">Learn More</button>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<p class="text-center mt-6">Check Out Our Contents</p>', unsafe_allow_html=True)
    st.markdown('<p class="text-center mb-6">Learn From The Experts</p>', unsafe_allow_html=True)

    st.markdown('<button class="bg-accent text-accent-foreground {BUTTON_CLASSES} mb-6">Stay In The Loop</button>', unsafe_allow_html=True)

    st.markdown('<form class="flex flex-col items-center mt-6">', unsafe_allow_html=True)
    st.markdown('<input type="email" placeholder="Enter your email" class="bg-input text-input placeholder-input p-2 rounded-md border border-border focus:outline-none focus:ring ring-ring transition-colors mb-2 w-full max-w-xs" />', unsafe_allow_html=True)
    st.markdown('<button type="submit" class="bg-primary text-primary-foreground py-2 px-4 rounded-md hover:bg-primary/80 transition-colors">Submit</button>', unsafe_allow_html=True)
    st.markdown('</form>', unsafe_allow_html=True)

    st.markdown('<p class="text-center mt-6 text-muted-foreground">All rights reserved</p>', unsafe_allow_html=True)
    st.markdown('<p class="text-center text-muted-foreground">Powered by</p>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Display the marketing expert component
marketing_expert_component()

# Streamlit component for embedding a digital marketing platform page
def digital_marketing_platform():
    st.markdown(
        """
        <div class="{} {} {}">
            <div class="{} {} {}">
                <h1 class="{} {} {}">Digital Marketing Platform</h1></div>
        </div>
        """.format(
            TW_CONTAINER, TW_TEXT_CENTER, TW_TEXT_LG,
            TW_RELATIVE, TW_H_FULL, TW_OVERFLOW_Y_AUTO,
            TW_TEXT_XL, TW_TEXT_BLUE, TW_MY_4,
            TW_TEXT_GRAY, TW_MY_4,
            TW_BG_BLUE, TW_TEXT_WHITE, TW_TEXT_CENTER, TW_TEXT_XL, TW_PX_4, TW_PY_2,
            TW_BG_WHITE, TW_TEXT_BLUE, TW_TEXT_CENTER, TW_TEXT_XL, TW_PX_4, TW_PY_2,
            TW_TEXT_GRAY, TW_TEXT_CENTER, TW_TEXT_XL
        ),
        unsafe_allow_html=True
    )

# Display the digital marketing platform component in the Streamlit app
digital_marketing_platform()