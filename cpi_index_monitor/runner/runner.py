from cpi_index_monitor.core.downloader import download
from cpi_index_monitor.sources.transparency_cpi import TransparencyCPI


def run_cpi(year=None):
    source = TransparencyCPI(year)

    print(f"Running CPI for year: {source.year}")

    file_url = source.get_latest_file()

    if not file_url:
        print("No report found.")
        return

    print(f"Downloading CPI file: {file_url}")

    download(file_url)