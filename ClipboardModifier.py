import pyperclip
import time


def monitor_and_clean_clipboard():
    previous_content = ""
    print("Clipboard Cleaner is now active.")

    while True:
        try:
            # Fetch the current clipboard content
            clipboard_content = pyperclip.paste()

            # Verify if the content is non-empty and has changed
            if clipboard_content and clipboard_content != previous_content:
                # Replace newlines with spaces and trim surrounding whitespace
                sanitized_content = clipboard_content.replace('\n', ' ').replace('\r', ' ').strip()

                # Update the clipboard only if modifications were made
                if sanitized_content != clipboard_content:
                    pyperclip.copy(sanitized_content)
                    print(f"Clipboard updated: {sanitized_content}")

                # Store the current content for future comparisons
                previous_content = clipboard_content

        except pyperclip.PyperclipException as clipboard_error:
            print(f"Clipboard access error: {clipboard_error}")

        except Exception as general_error:
            print(f"An unexpected error occurred: {general_error}")

        # Pause briefly to reduce CPU usage
        time.sleep(0.5)


if __name__ == "__main__":
    try:
        monitor_and_clean_clipboard()
    except KeyboardInterrupt:
        print("Clipboard Cleaner has been stopped.")
