"""
Entrypoint and CLI orchestration for BLE/Wi-Fi Scanner.
Handles argument parsing, event loop, and calls main scanning/plotting logic.
"""

from ble_wifi_scanner.config import *
from ble_wifi_scanner.scanners import start_scan_loops
from ble_wifi_scanner.plotting import initialize_plot, update_ploasync def main():

import argparse
import asyncio

def parse_args():
    parser = argparse.ArgumentParser(description="BLE/Wi-Fi Scanner CLI")
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')
    parser.add_argument('--scan-duration', type=int, default=60, help='Scan duration in seconds')
    return parser.parse_args()

async def main(args):
    if args.debug:
    
        import logging
        logging.basicConfig(level=logging.DEBUG)
    initialize_plot()
    # Start the scan loop(s)
    scan_task = asyncio.create_task(start_scan_loops(args.scan_duration))
    async def main():
        try:
        await scan_task
    except KeyboardInterrupt:
        print("Scan interrupted. Exiting...")
if __name__ == "__main__":
    args = parse_args()
    asyncio.run(main(args))
