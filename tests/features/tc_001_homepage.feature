Feature: Website homepage loads successfully

  Scenario: Homepage loads without errors
    Given The user has a stable internet connection and a modern web browser
    When The user navigates to https://www.emids.com/
    Then The homepage loads completely with all visible content such as header, hero section, navigation menu, footer, and branding elements rendered correctly without any obvious errors, broken layouts, or missing resources

  Scenario: Homepage loads with all media assets
    Given The user has opened the website homepage
    When The page finishes loading
    Then All images, icons, videos, and media assets are visible and properly displayed without placeholder icons or missing resource errors

  Scenario: Homepage loads CSS and JavaScript correctly
    Given The user has navigated to the homepage
    When The page loads
    Then Styles are applied correctly and interactive elements are functional without JavaScript errors displayed in the browser console
