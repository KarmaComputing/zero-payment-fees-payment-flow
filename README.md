# Zero Fees Payment Collection

> This approach may be suitable for business-to-business (B2B) payments which want an alternative to paying opaque and complicated card fees. This approach has the advantage of zero transaction fees, but is more suited to B2B transactions as it required the bill payer to provide a payment reference- something businesses are very familar with.

Takes advantage of 'developments' in Open Banking whereby modern
banks offer API access **to individual account holders** (not via
a Payment-Information-Service-Provider ([PISP](https://www.fca.org.uk/consumers/account-information-payment-initiation-services))). In other words, you don't need to go via Plaid, Truelayer etc or other PISPs if you have simple payment requirements and simply want an alternative to often opaque and complicated card fees [1](https://www.ecb.europa.eu/press/pubbydate/2019/html/ecb.cardpaymentsineu_currentlandscapeandfutureprospects201904~30d4de2fc4.en.html), [2](https://www.thisismoney.co.uk/money/smallbusiness/article-14189365/UK-businesses-set-EU-customers-plans-slash-harmful-200m-year-card-fees.html), [3](https://www.theguardian.com/australia-news/2024/sep/14/australia-card-surcharges-credit-debt-rba-review).

Allows a payment flow which:

- Promts bill payer to make a payment to the company bank account
- The bill payer must use the reference presented to them
- In the background, the bank acount transactions are ['polled'](https://en.wikipedia.org/wiki/Polling_(computer_science)) to check for the existance
of the payment
- The payment is considered complete when/if if the payment reference, and amount match.

The payment flow has advantages in that it:

- Incurs zero fees for the company accepting the payments (assuming bank transfer payments are free, which is usually the case)
- Requires no storage of customer payment information
- Allows companies operating on small margins to compete, where a credit card processing fee (1% - 2% and higher) can significantly eat into margins

The payment flow has disadvantages in that it:

- Is a payment flow less familiar to customers (but arguably quite familiar to commercial payments/financial controllers where requiring a payment reference is
  standard practice)


# Compatible banks

- Any UK bank which provided API access **to it's account holders** is compatible
  with this payment pattern.
- The code here demonstrates the pattern using Starling Bank. The same pattern appears to be possible with Monzo bank (because the pattern has been seen used by vendors using that bank also).

# Want some help?

Would you like to implement this approach in your business?
Feel free to reach out for support implementing this payment flow in your business.
