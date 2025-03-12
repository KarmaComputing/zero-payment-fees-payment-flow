#!/usr/bin/env python3
"""
Zero-Fees Payment Collection System

A Flask-based application that provides payment processing functionality
without charging additional fees. This system allows for creating payments,
processing them, and checking their status.
"""

from flask import Flask, render_template, jsonify, request
import requests
import os
import logging
from datetime import datetime

log = logging.getLogger()
handler = logging.StreamHandler()  # sys.stderr will be used by default

PYTHON_LOG_LEVEL = os.getenv("PYTHON_LOG_LEVEL", logging.DEBUG)
PERSONAL_ACCESS_TOKEN = os.getenv("PERSONAL_ACCESS_TOKEN")
BANK_ACCOUNT_ID = os.getenv("BANK_ACCOUNT_ID")

# Setup logging
log.setLevel(PYTHON_LOG_LEVEL)
handler.setLevel(PYTHON_LOG_LEVEL)
handler.setFormatter(
    logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)-8s %(message)s %(funcName)s %(pathname)s:%(lineno)d"  # noqa: E501
    )
)
log.addHandler(handler)

headers = {
    "Authorization": PERSONAL_ACCESS_TOKEN,
    "accept": "application/json",
}
# End Setup logging


app = Flask(__name__)


@app.route("/")
def index():
    expected_payment_reference = None
    if request.args.get("expected_payment_reference"):
        expected_payment_reference = request.args.get(
            "expected_payment_reference"
        )  # noqa: E501
    return render_template(
        "index.html", expected_payment_reference=expected_payment_reference
    )


@app.route("/check-payment-status/<expected_payment_reference>")
def check_payment_status(expected_payment_reference) -> bool:
    bool_located_payment_reference = False

    # startDate = "yyyy-mm-dd"
    # endDate = "yyyy-mm-dd"
    todayFormatted = datetime.now().strftime("%Y-%m-%d")
    minTransactionTimestamp = f"{todayFormatted}T00:00:00.000Z"
    maxTransactionTimestamp = f"{todayFormatted}T23:59:59.000Z"
    host = f"https://api.starlingbank.com/api/v2/feed/account/{BANK_ACCOUNT_ID}/settled-transactions-between"  # noqa: E501
    host += f"?minTransactionTimestamp={minTransactionTimestamp}"
    host += f"&maxTransactionTimestamp={maxTransactionTimestamp}"

    headers["accept"] = "application/json"
    req = requests.get(host, headers=headers)
    resp = req.json()

    for feedItem in resp["feedItems"]:
        bank_transaction_reference = feedItem.get("reference")
        log.info(
            f'Looking for payment reference "{expected_payment_reference}"'
        )  # noqa: E501
        if bank_transaction_reference == expected_payment_reference:
            bool_located_payment_reference = True
            log.info(
                "Found matching payment reference "
                f'"{expected_payment_reference}"'  # noqa: E501
            )  # noqa E501

    resp = {"msg": {"located_payment_status": bool_located_payment_reference}}
    return jsonify(resp)
