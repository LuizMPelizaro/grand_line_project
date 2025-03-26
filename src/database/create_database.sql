CREATE
DATABASE raw_data;

----- Tabela de pesquisa por ação
-- Request https://brapi.dev/api/quote/PETR4?range=1mo&interval=1d&modules=summaryProfile&token=
-- Retorna o valor das açoes e seu summary profile (Informações sovbre a empresa)

CREATE TABLE "raw_quote"
(
    "currency"                     VARCHAR(3) NOT NULL,
    "market_cap"                   NUMERIC    NOT NULL,
    "short_name"                   VARCHAR    NOT NULL,
    "long_name"                    VARCHAR    NOT NULL,
    "regular_market_change"        NUMERIC    NOT NULL,
    "regular_market_change_percent" NUMERIC    NOT NULL,
    "regular_market_time"          TIMESTAMP  NOT NULL,
    "regular_market_price"         MONEY      NOT NULL,
    "regular_market_day_high"      MONEY      NOT NULL,
    "regular_market_day_range"     VARCHAR    NOT NULL,
    "regular_market_day_low"       MONEY      NOT NULL,
    "regular_market_volume"        BIGINT     NOT NULL,
    "regular_market_previous_close" MONEY      NOT NULL,
    "regular_market_open"          MONEY      NOT NULL,
    "fifty_two_week_range"         VARCHAR    NOT NULL,
    "fifty_two_week_low"           MONEY      NOT NULL,
    "fifty_two_week_high"          MONEY      NOT NULL,
    "symbol"                       VARCHAR    NOT NULL,
    "historical_data_price"        JSONB,
    "summary_profile"              JSONB,
    "price_earnings"               MONEY      NOT NULL,
    "earnings_per_share"           NUMERIC,
    "logo_url"                     VARCHAR
);


-- Lista de indicadores de país : bovespa , dow jones e existem a quotas ...

CREATE TABLE "index_list"
(
    "stock" VARCHAR NOT NULL,
    "name"  VARCHAR NOT NULL
);

-- Lista de ações

CREATE TABLE "quota_list"
(
    "stock"      VARCHAR NOT NULL,
    "name"       VARCHAR NOT NULL,
    "close"      NUMERIC NOT NULL,
    "change"     NUMERIC NOT NULL,
    "volume"     BIGINT  NOT NULL,
    "market_cap" BIGINT,
    "logo"       VARCHAR NOT NULL,
    "sector"     VARCHAR NOT NULL,
    "type"       VARCHAR NOT NULL
);




