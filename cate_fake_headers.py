# from fake_headers import Headers
from fake_headers import Headers

if __name__ == "__main__":
    header = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate ony Windows platform
        headers=True,  # generate misc headers
    )

    for i in range(1):
        print(header.generate())
