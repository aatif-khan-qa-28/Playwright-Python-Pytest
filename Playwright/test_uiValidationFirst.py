import re

from playwright.sync_api import Page, expect


def test_UIvalidationDynamicScript(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # sign in steps
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    # cart steps
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()
    nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    page.locator(".media-heading").filter(has_text="iphone X").is_visible()
    page.locator(".media-heading").filter(has_text="Nokia Edge").is_visible()


def test_childWindowHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage_Info:
        page.locator(".blinkingText").click()
        child_window = newPage_Info.value
        print("New Page Value : ", child_window)
        text = child_window.locator(".red").text_content()
        # email = re.search(r"\S+@\S+", text)
        # print(email.group() if email else "No email found")
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"
