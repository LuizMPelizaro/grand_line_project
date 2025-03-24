CREATE
DATABASE 'raw_data';


CREATE
DATABASE raw_data;

----- Tabela de pesquisa por ação
-- Request https://brapi.dev/api/quote/PETR4?range=1mo&interval=1d&modules=summaryProfile&token=
-- Retorna o valor das açoes e seu summary profile (Informações sovbre a empresa)

CREATE TABLE "raw_quote"
(
    "currency"                   VARCHAR(3) NOT NULL,
    "marketCap"                  BIGINT     NOT NULL,
    "shortName"                  VARCHAR    NOT NULL,
    "longName"                   VARCHAR    NOT NULL,
    "regularMarketChange"        NUMERIC    NOT NULL,
    "regularMarketChangePercent" NUMERIC    NOT NULL,
    "regularMarketTime"          TIMESTAMP  NOT NULL,
    "regularMarketPrice"         MONEY      NOT NULL,
    "regularMarketDayHigh"       MONEY      NOT NULL,
    "regularMarketDayRange"      VARCHAR    NOT NULL,
    "regularMarketDayLow"        MONEY      NOT NULL,
    "regularMarketVolume"        BIGINT     NOT NULL,
    "regularMarketPreviousClose" MONEY      NOT NULL,
    "regularMarketOpen"          MONEY      NOT NULL,
    "fiftyTwoWeekRange"          VARCHAR    NOT NULL,
    "fiftyTwoWeekLow"            MONEY      NOT NULL,
    "fiftyTwoWeekHigh"           MONEY      NOT NULL,
    "symbol"                     VARCHAR    NOT NULL,
    "historicalDataPrice"        JSONB,
    "summaryProfile"             JSONB,
    "priceEarnings"              MONEY      NOT NULL,
    "earningsPerShare"           NUMERIC,
    "logourl"                    VARCHAR
)


-- Lista de indicadores de país : bovespa , dow jones e existem a quotas ...

CREATE TABLE "index_list"
(
    "stock" VARCHAR NOT NULL,
    "name"  VARCHAR NOT NULL
)

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
)




