from app.commons.config.app_config import AppConfig, Secret


def create_app_config() -> AppConfig:
    """
    Create AppConfig for staging environment
    """
    return AppConfig(
        ENVIRONMENT="staging",
        DEBUG=False,
        NINOX_ENABLED=True,
        METRICS_CONFIG={"service_name": "payment-service", "cluster": "staging"},
        TEST_SECRET=Secret(name="hello_world_secret"),
        PAYIN_MAINDB_URL=Secret(name="payin_maindb_url"),
        PAYIN_PAYMENTDB_URL=Secret(name="payin_paymentdb_url"),
        PAYOUT_MAINDB_URL=Secret(name="payout_maindb_url"),
        PAYOUT_BANKDB_URL=Secret(name="payout_bankdb_url"),
        LEDGER_MAINDB_URL=Secret(name="ledger_maindb_url"),
        LEDGER_PAYMENTDB_URL=Secret(name="ledger_paymentdb_url"),
        STRIPE_US_SECRET_KEY=Secret(name="stripe_us_secret_key"),
        STRIPE_US_PUBLIC_KEY=Secret(name="stripe_us_public_key"),
    )