Feature: Mobile responsive view functionality

  Scenario: Mobile viewport renders correctly
    Given The user opens the website in a mobile-sized browser window with viewport width of 375px
    When The homepage loads in mobile view
    Then Text is readable without horizontal scrolling, images scale appropriately, the menu transforms to a mobile menu icon, and all buttons are visible and properly sized for touch interaction

  Scenario: Mobile hamburger menu opens and functions
    Given The user is on the homepage in mobile view
    When The user taps on the hamburger menu icon
    Then The mobile navigation menu slides out or expands showing all menu items that can be tapped to navigate to their respective pages

  Scenario: Contact form is mobile-friendly
    Given The user has navigated to the contact form on a mobile device
    When The user attempts to fill in form fields and submit
    Then Form fields are easily tappable, input keyboards open appropriately, and the submit button is prominently visible and functional

  Scenario: Images resize appropriately on mobile
    Given The user is viewing the homepage on a mobile device
    When The page loads with all hero images and content images
    Then Images are optimized for mobile display, do not overflow the screen width, and maintain aspect ratio without distortion

  Scenario: Content is readable on tablet viewport
    Given The user opens the website in a tablet-sized browser window with viewport width of 768px
    When The homepage loads
    Then Layout adjusts appropriately for tablet with readable text, visible images, accessible menu, and properly sized buttons without excessive white space or crowding

  Scenario: Touch interactions work without pinch zoom issues
    Given The user is on the homepage in mobile view
    When The user taps on buttons and links
    Then Touch targets are appropriately sized minimum 44x44 pixels, and no accidental zooming occurs during normal navigation
