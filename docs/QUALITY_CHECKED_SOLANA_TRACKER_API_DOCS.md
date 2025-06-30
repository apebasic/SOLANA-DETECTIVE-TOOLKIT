# SOLANA TRACKER API - QUALITY CHECKED DOCUMENTATION

**Base URL**: `https://data.solanatracker.io`
**Authentication**: x-api-key header required
**Total Endpoints**: 44
**Last Updated**: 2025-06-28 (Quality Checked)

## COMPLETE API REFERENCE (QUALITY CHECKED)

## Token Endpoints

### GET /tokens/{tokenAddress}

**Description**: Retrieves comprehensive information about a specific token.

**Path Parameters**:
- `tokenAddress` (required): The tokenAddress identifier

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"token":{
"name":"OFFICIAL TRUMP",
"symbol":"TRUMP",
"mint":"6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN",
"uri":"https://arweave.net/cSCP0h2n1crjeSWE9KF-XtLciJalDNFs7Vf-Sm0NNY0",
"decimals":6,
"description":"",
"image":"https://image.solanatracker.io/proxy?url=https%3A%2F%2Farweave.net%2FVQrPjACwnQRmxdKBTqNwPiyo65x7LAT773t8Kd7YBzw",
"hasFileMetaData":true,
"strictSocials":{
```

---

### GET /tokens/by-pool/{poolAddress}

**Path Parameters**:
- `poolAddress` (required): The poolAddress identifier

**Pagination**: Supported (cursor-based)

---

### GET /tokens/{tokenAddress}/holders

**Description**: Gets the top 100 holders for a specific token and the total amount

**Path Parameters**:
- `tokenAddress` (required): The tokenAddress identifier

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"total":651343,
"accounts":[
{
"wallet":"2RH6rUTPBJ9rUDPpuV9b8z1YL56k1tYU6Uk5ZoaEFFSK",
"amount":800000022.564,
"value":{
"quote":8134085180.01063,
"usd":8134085180.01063
},
"percentage":80.00004595161334
},
{
"wallet":"9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM",
"amount":25151426.025001,
"value":{
"quote":255729794.894759,
"usd":255729794.894759
},
"percentage":2.5151439762462187
},
{
"wallet":"C68a6RCGLiPskbPYtAcsCjhG8tfTWYcoB4JjCrXFdqyo",
"amount":15978104.518764,
"value":{
"quote":162459074.3812657,
"usd":162459074.3812657
},
"percentage":1.5978113245847323
},
}
```

---

### GET /tokens/{tokenAddress}/holders/top

**Description**: Gets the top 20 holders for a token.

**Path Parameters**:
- `tokenAddress` (required): The tokenAddress identifier

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"address": "FwbBBzAfBgGaAWjEG4nprZQ8mp8w2W3eHLxAWbyUnwXR",
"amount": 114837224.78981262,
"percentage": 12.897608531935292,
"value": {
"quote": 364.490083024,
"usd": 80016.91106116588
}
},
{
"address": "Cst5bqk7QJAj1tR7qH9eiYnT7ygDEashKYTFvV1obRGK",
"amount": 27748733.327190395,
"percentage": 3.116518187950125,
"value": {
"quote": 88.07368980529128,
"usd": 19334.914534601114
}
}
]
```

---

### GET /tokens/{tokenAddress}/ath

**Description**: Retrieves the all-time high price of a token (since the data API started recording).

**Path Parameters**:
- `tokenAddress` (required): The tokenAddress identifier

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"highest_price": 0.002399892080590551,
"timestamp": 171924662484
}
```

---

### GET /tokens/latest

**Description**: Retrieves the latest 100 tokens.

**Query Parameters**:
- `page` (optional): Page number (default: 1)
- `limit` (optional): Number of items per page (default: 250, max: 500)

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"token": {
"name": "April Fool’s Day",
"symbol": "FOOLS",
"mint": "DWKaYT4omXcZeDiaAUoJfBMhDK7DDQTymusKohsGpump",
"uri": "https://ipfs.io/ipfs/QmWR8ah9MmciD3ErUJDb9csfRoyFHTT5Lves2zSnqXPeYz",
"decimals": 6,
"hasFileMetaData": true,
"createdOn": "https://pump.fun",
"description": "It’s a celebration!",
"image": "https://image.solanatracker.io/proxy?url=https%3A%2F%2Fimage.solanatracker.io%2Fproxy%3Furl%3Dhttps%253A%252F%252Fipfs.io%252Fipfs%252FQmbBVm7CffYX2wnuCrGLARgQHAoX79E4m1HWN2AcBqGYqa",
"showName": true,
"twitter": "https://twitter.com/aprilfoolsday",
"telegram": "https://t.me/aprilsfoolsday",
"strictSocials": {
"twitter": "https://twitter.com/aprilfoolsday",
"telegram": "https://t.me/aprilsfoolsday"
},
"creation": {
"creator": "9zGpUxJr2jnkwSSF9VGezy6aALEfxysE19hvcRSkbn15",
"created_tx": "5eHbuGuF1GfFcBgHcym69A1ErUYzY5vD2tE5hJ4A71yvZ7U3e93xMy1CWeH1HcAiyy6Yi8GDoJjeSXHhuDC4CFnW",
"created_time": 1749298225
}
},
"pools": [],
"events": {},
"risk": {},
"buys": 3,
"sells": 0,
"txns": 3
},
{
"token": {
"name": "KWGPOK",
"symbol": "OKGWP",
"mint": "7HKHmpYMVtwMqwLrH5529q26v8grmUmWscmww97pump",
"uri": "https://ipfs.io/ipfs/QmTBkpB8t7R5R9aR2tcJxAM4PM3R6XB9VZ2jE2i1wQR5ar",
"decimals": 6,
"hasFileMetaData": true,
"createdOn": "https://pump.fun",
"description": "POGWSE",
"image": "https://image.solanatracker.io/proxy?url=https%3A%2F%2Fimage.solanatracker.io%2Fproxy%3Furl%3Dhttps%253A%252F%252Fipfs.io%252Fipfs%252FQmRDA43fShZSVCE73wSbKemivVPYqWhW222n5roH8c987w",
"showName": true,
"strictSocials": {},
"creation": {
"creator": "9zGpUxJr2jnkwSSF9VGezy6aALEfxysE19hvcRSkbn15",
"created_tx": "5eHbuGuF1GfFcBgHcym69A1ErUYzY5vD2tE5hJ4A71yvZ7U3e93xMy1CWeH1HcAiyy6Yi8GDoJjeSXHhuDC4CFnW",
"created_time": 1749298225
}
},
"pools": [
{
"poolId": "7HKHmpYMVtwMqwLrH5529q26v8grmUmWscmww97pump",
"liquidity": {
"quote": 60.200984914,
"usd": 7504.35662608982
},
"price": {
"quote": 2.814661839287826e-8,
"usd": 0.000003508618049029575
},
"tokenSupply": 1000000000,
"lpBurn": 100,
"tokenAddress": "7HKHmpYMVtwMqwLrH5529q26v8grmUmWscmww97pump",
"marketCap": {
"quote": 28.14661839287826,
"usd": 3508.618049029575
},
"decimals": 6,
"security": {
"freezeAuthority": null,
"mintAuthority": null
},
"quoteToken": "So11111111111111111111111111111111111111112",
"market": "pumpfun",
"curvePercentage": 0.45168079312482234,
"curve": "Hf4ak2796LJu4nYFUyVAmXV7bxiSvLw3Ayq5C4PFDJWk",
"deployer": "6hepaQw3pugEBnwY2JBuYGoE5kZjho4DCSHAUKZhcoe",
"lastUpdated": 1743276573362,
"createdAt": 1743276571192,
"txns": {
"buys": 2,
"total": 4,
"volume": 251,
"sells": 1
}
}
"events": {
"1m": {
"priceChangePercentage": 0
},
"5m": {
"priceChangePercentage": 0
},
"15m": {
"priceChangePercentage": 0
},
"30m": {
"priceChangePercentage": 0
},
"1h": {
"priceChangePercentage": 0
},
"2h": {
"priceChangePercentage": 0
},
"3h": {
"priceChangePercentage": 0
},
"4h": {
"priceChangePercentage": 0
},
"5h": {
"priceChangePercentage": 0
},
"6h": {
"priceChangePercentage": 0
},
"12h": {
"priceChangePercentage": 0
},
"24h": {
"priceChangePercentage": 0
}
},
"risk": {
"rugged": false,
"risks": [
{
"name": "No social media",
"description": "This token has no social media links",
"level": "warning",
"score": 2000
},
{
"name": "Pump.fun contracts can be changed at any time",
"description": "Pump.fun contracts can be changed by Pump.fun at any time",
"level": "warning",
"score": 10
},
{
"name": "Bonding curve not complete",
"description": "No raydium liquidity pool, bonding curve not complete",
"level": "warning",
"score": 4000
}
"score": 5
},
"buys": 3,
"sells": 1,
"txns": 4
}
]
```

---

### POST /tokens/multi

**Pagination**: Supported (cursor-based)

**Notes**:
- Batch endpoint for multiple items

---

### GET /tokens/trending

**Description**: Gets the top 100 trending tokens based on transaction volume in the specified timeframe (default: past hour).

**Pagination**: Supported (cursor-based)

---

### GET /tokens/trending/{timeframe}

**Description**: Gets the top 100 trending tokens based on transaction volume in the specified timeframe (default: past hour).

**Path Parameters**:
- `timeframe` (required): The timeframe identifier

**Pagination**: Supported (cursor-based)

---

### GET /tokens/volume

**Description**: Retrieves the top 100 tokens sorted by highest volume within the specified timeframe.

**Pagination**: Supported (cursor-based)

---

### GET /tokens/volume/{timeframe}

**Description**: Retrieves the top 100 tokens sorted by highest volume within the specified timeframe.

**Path Parameters**:
- `timeframe` (required): The timeframe identifier

**Pagination**: Supported (cursor-based)

---

### GET /tokens/multi/all

**Description**: Gets an overview of latest, graduating, and graduated tokens (Pumpvision / Photon Memescope style).

**Pagination**: Supported (cursor-based)

**Notes**:
- Batch endpoint for multiple items

**Response Example**:
```json
{
"latest": [
{
"token": {
"name": "Cult of Trenching",
"symbol": "TrenchCult",
"mint": "uwjFzyPjn8ayhfVfeMUzkQBbrgeFMeEd47NvRbCpump",
"uri": "https://ipfs.io/ipfs/QmWT5HsQh5oLvnqthDgQEGVUjn3gH9R6PyhJNr4wkdsn66",
"decimals": 6,
"hasFileMetaData": true,
"createdOn": "https://pump.fun",
"description": "",
"image": "https://image.solanatracker.io/proxy?url=https%3A%2F%2Fimage.solanatracker.io%2Fproxy%3Furl%3Dhttps%253A%252F%252Fipfs.io%252Fipfs%252FQmXWHqMvrqkubp6kxw9vUcNPv42ZXQ3BLcCARXjUoWLsAg",
"showName": true,
"twitter": "https://x.com/solgoated1/status/1906065859657032002",
"website": "https://x.com/solgoated1/status/1906065859657032002",
"strictSocials": {
"twitter": "https://x.com/solgoated1/status/1906065859657032002"
}
},
"pools": [
{
"poolId": "uwjFzyPjn8ayhfVfeMUzkQBbrgeFMeEd47NvRbCpump",
"liquidity": {
"quote": 74.997144066,
"usd": 9366.628111886268
},
"price": {
"quote": 4.3682600325215646e-8,
"usd": 0.0000054556567093592755
},
"tokenSupply": 1000000000,
"lpBurn": 100,
"tokenAddress": "uwjFzyPjn8ayhfVfeMUzkQBbrgeFMeEd47NvRbCpump",
"marketCap": {
"quote": 43.682600325215645,
"usd": 5455.656709359276
},
"decimals": 6,
"security": {
"freezeAuthority": null,
"mintAuthority": null
},
"quoteToken": "So11111111111111111111111111111111111111112",
"market": "pumpfun",
"curvePercentage": 27.05425691727814,
"curve": "7ofQyZf2HmYCmM4LWHNaP9VEZ2frevtwmEdtjBb2hwgh",
"deployer": "6Y5FiURYwKGXBPAes1P9WDGuHoi8oiz4FwYWyHeYNXPw",
"lastUpdated": 1743276647681,
"createdAt": 1743276646913,
"txns": {
"buys": 3,
"total": 3,
"volume": 490,
"sells": 0
}
}
"events": {
"1m": {
"priceChangePercentage": 0
},
"5m": {
"priceChangePercentage": 0
},
"15m": {
"priceChangePercentage": 0
},
"30m": {
"priceChangePercentage": 0
},
"1h": {
"priceChangePercentage": 0
},
"2h": {
"priceChangePercentage": 0
},
"3h": {
"priceChangePercentage": 0
},
"4h": {
"priceChangePercentage": 0
},
"5h": {
"priceChangePercentage": 0
},
"6h": {
"priceChangePercentage": 0
},
"12h": {
"priceChangePercentage": 0
},
"24h": {
"priceChangePercentage": 0
}
},
"risk": {
"rugged": false,
"risks": [
{
"name": "Pump.fun contracts can be changed at any time",
"description": "Pump.fun contracts can be changed by Pump.fun at any time",
"level": "warning",
"score": 10
},
{
"name": "Bonding curve not complete",
"description": "No raydium liquidity pool, bonding curve not complete",
"level": "warning",
"score": 4000
}
"score": 3
},
"buys": 2,
"sells": 0,
"txns": 2
}
"graduating": [
{
"token": {
"name": "White Grandpa",
"symbol": "UNC",
"mint": "6wX5EfAx9gGHLQ2Z21N8CaLorGav8EFDdrTzyq1pump",
"uri": "https://ipfs.io/ipfs/QmPX3mqev2udUJLVNFHTxY8gTSodDbfbQrYoQvAWq9FVsT",
"decimals": 6,
"hasFileMetaData": true,
"createdOn": "https://pump.fun",
"description": "stay woke\r\nhttps://x.com/DailyLoud/status/1905634722543251595",
"image": "https://image.solanatracker.io/proxy?url=https%3A%2F%2Fipfs-forward.solanatracker.io%2Fipfs%2FQmRY15KCq65MMgECXWbnAivuDcHV7t7gKXHRpb2qCQbeGM",
"showName": true,
"twitter": "https://x.com/DailyLoud/status/1905634722543251595",
"strictSocials": {
"twitter": "https://x.com/DailyLoud/status/1905634722543251595"
},
"creation": {
"creator": "9zGpUxJr2jnkwSSF9VGezy6aALEfxysE19hvcRSkbn15",
"created_tx": "5eHbuGuF1GfFcBgHcym69A1ErUYzY5vD2tE5hJ4A71yvZ7U3e93xMy1CWeH1HcAiyy6Yi8GDoJjeSXHhuDC4CFnW",
"created_time": 1749298225
}
},
"pools": [
{
"poolId": "6wX5EfAx9gGHLQ2Z21N8CaLorGav8EFDdrTzyq1pump",
"liquidity": {
"quote": 184.205822434,
"usd": 23006.041846940676
},
"price": {
"quote": 2.635273705842488e-7,
"usd": 0.00003291275832308565
},
"tokenSupply": 1000000000,
"lpBurn": 100,
"tokenAddress": "6wX5EfAx9gGHLQ2Z21N8CaLorGav8EFDdrTzyq1pump",
"marketCap": {
"quote": 263.5273705842488,
"usd": 32912.75832308565
},
"decimals": 6,
"security": {
"freezeAuthority": null,
"mintAuthority": null
},
"quoteToken": "So11111111111111111111111111111111111111112",
"market": "pumpfun",
"curvePercentage": 91.22426412249791,
"curve": "B8UVQ46EqQ2sEHagX7h1WzDpxuFVXp6fAjiXFaT1D692",
"deployer": "4VfBaC9Jftw4Bm1oHYt8TrhamF7DGEr9Ut2JovCPWbqe",
"lastUpdated": 1743276647759,
"createdAt": 1743274179758,
"txns": {
"buys": 977,
"total": 1866,
"volume": 31100,
"sells": 889
},
"bundleId": "e88d7ab51773355bad96ac842f0976231bd87083d77882f56c62a277c840fcb8"
}
"events": {
"1m": {
"priceChangePercentage": -4.1724840124786216
},
"5m": {
"priceChangePercentage": -0.8171310506410367
},
"15m": {
"priceChangePercentage": 46.42260473798215
},
"30m": {
"priceChangePercentage": 54.14793685627088
},
"1h": {
"priceChangePercentage": 868.7250909621494
},
"2h": {
"priceChangePercentage": 868.7250909621494
},
"3h": {
"priceChangePercentage": 868.7250909621494
},
"4h": {
"priceChangePercentage": 868.7250909621494
},
"5h": {
"priceChangePercentage": 868.7250909621494
},
"6h": {
"priceChangePercentage": 868.7250909621494
},
"12h": {
"priceChangePercentage": 868.7250909621494
},
"24h": {
"priceChangePercentage": 868.7250909621494
}
},
"risk": {
"rugged": false,
"risks": [
{
"name": "Pump.fun contracts can be changed at any time",
"description": "Pump.fun contracts can be changed by Pump.fun at any time",
"level": "warning",
"score": 10
},
{
"name": "Bonding curve not complete",
"description": "No raydium liquidity pool, bonding curve not complete",
"level": "warning",
"score": 4000
}
"score": 3
},
"buys": 1182,
"sells": 1123,
"txns": 2305,
"holders": 232
}
"graduated": [
{
"token": {
"name": "X Æ Meow-12",
"symbol": "XÆMeow-12",
"mint": "UkAivL55R7iBEW3wfsTETdiHM1jfByHTRAFQHiKWLyF",
"uri": "https://ipfs-forward.solanatracker.io/ipfs/QmZc1ndhGNpywi5YdbiUwWetAumWPCqdyHCDoAN6hVQ7Pb",
"decimals": 6,
"description": "",
"image": "https://image.solanatracker.io/proxy?url=https%3A%2F%2Fipfs-forward.solanatracker.io%2Fipfs%2FQme3Qoomq5sUxx8E7BViGQ5CCs9obGHWfA8C6UrmBscPSS",
"showName": true,
"createdOn": "https://pump.fun",
"twitter": "https://x.com/Josikinz/status/1906060748796867071",
"hasFileMetaData": true,
"strictSocials": {
"twitter": "https://x.com/Josikinz/status/1906060748796867071"
},
"creation": {
"creator": "9zGpUxJr2jnkwSSF9VGezy6aALEfxysE19hvcRSkbn15",
"created_tx": "5eHbuGuF1GfFcBgHcym69A1ErUYzY5vD2tE5hJ4A71yvZ7U3e93xMy1CWeH1HcAiyy6Yi8GDoJjeSXHhuDC4CFnW",
"created_time": 1749298225
}
},
"pools": [
{
"poolId": "5UH61hrcBSgE3fLXQ4bMTtXb7e1bVvSeisJq7z8V8yvE",
"liquidity": {
"quote": 18.503268912,
"usd": 4613.051725397854
},
"price": {
"quote": 1.9289130860019372e-8,
"usd": 0.0000024044875210544464
},
"tokenSupply": 1000000000,
"lpBurn": 100,
"tokenAddress": "UkAivL55R7iBEW3wfsTETdiHM1jfByHTRAFQHiKWLyF",
"marketCap": {
"quote": 19.289130860019373,
"usd": 2404.4875210544465
},
"decimals": 6,
"security": {
"freezeAuthority": null,
"mintAuthority": null
},
"quoteToken": "So11111111111111111111111111111111111111112",
"market": "pumpfun-amm",
"deployer": "2WDizMKyQaYXJxaZ2oPFGM9kdCZuWhX52oMy57NUESrN",
"lastUpdated": 1743276422531,
"txns": {
"buys": 25,
"total": 45,
"volume": 5947,
"sells": 20
},
"bundleId": "5ad775152feacf1be43bdbc82a9c0551a2757cca30bb8bfb15c0d1742692a78e"
},
{
"poolId": "UkAivL55R7iBEW3wfsTETdiHM1jfByHTRAFQHiKWLyF",
"liquidity": {
"quote": 0,
"usd": 0
},
"price": {
"quote": null,
"usd": null
},
"tokenSupply": 1000000000,
"lpBurn": 100,
"tokenAddress": "UkAivL55R7iBEW3wfsTETdiHM1jfByHTRAFQHiKWLyF",
"marketCap": {
"quote": null,
"usd": null
},
"decimals": 6,
"security": {
"freezeAuthority": null,
"mintAuthority": null
},
"quoteToken": "So11111111111111111111111111111111111111112",
"market": "pumpfun",
"curvePercentage": 100,
"curve": "WLEgumwUg9brqWHZUYPFVpSqAur5Av8ctYkqegtUDJN",
"deployer": "6d22FozaKK239PoBYVffkYKA1QPQZE8fC7AQkpmHQfjp",
"lastUpdated": 1743275416731,
"createdAt": 1743275416459,
"txns": {
"buys": 1,
"total": 1,
"volume": 5305,
"sells": 0
}
}
"events": {
"1m": {
"priceChangePercentage": 0
},
"5m": {
"priceChangePercentage": 2.546993067700225
},
"15m": {
"priceChangePercentage": -7.955395053691079
},
"30m": {
"priceChangePercentage": -95.75161080372789
},
"1h": {
"priceChangePercentage": -95.75161080372789
},
"2h": {
"priceChangePercentage": -95.75161080372789
},
"3h": {
"priceChangePercentage": -95.75161080372789
},
"4h": {
"priceChangePercentage": -95.75161080372789
},
"5h": {
"priceChangePercentage": -95.75161080372789
},
"6h": {
"priceChangePercentage": -95.75161080372789
},
"12h": {
"priceChangePercentage": -95.75161080372789
},
"24h": {
"priceChangePercentage": -95.75161080372789
}
},
"risk": {
"rugged": false,
"risks": [
{
"name": "Price Decrease",
"description": "Price decreased by more than 50% in the last 24 hours",
"level": "warning",
"score": 1000
}
"score": 1
},
"buys": 1,
"sells": 0,
"txns": 1,
"holders": 13
}
]
}
```

---

### GET /tokens/multi/graduated

**Pagination**: Supported (cursor-based)

**Notes**:
- Batch endpoint for multiple items

---

## Price Endpoints

### GET /price

**Description**: Gets price information for a single token.

**Query Parameters**:
- `token` (required): The token address
- `priceChanges` (optional): Returns price change percentages up to 24 hours ago

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"price": 1.23,
"liquidity": 1000000,
"marketCap": 50000000,
"lastUpdated": 1628097600000
}
```

---

### GET /price/history

**Description**: Gets historic price information for a single token.

**Query Parameters**:
- `token` (required): The token address
- `time_from` (required): Start time (unix timestamp)
- `time_to` (required): End time (unix timestamp)

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"current": 0.00153420295896641,
"3d": 0.0003172284163334442,
"5d": 0.00030182128340039925,
"7d": 0.0003772164702056164,
"14d": 0.0003333105740474755,
"30d": 0.0008621030248959815
}
```

---

### GET /price/history/timestamp

**Description**: Gets specific historic price information for a token at a given timestamp.

**Query Parameters**:
- `token` (required): The token address
- `timestamp` (required): Unix timestamp

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"price": 0.0010027648651222173,
"timestamp": 1732237829688,
"timestamp_unix": 1732237830,
"pool": "D5Nbd1N7zAu8zjKoz3yR9WSXTiZr1c1TwRtiHeu5j7iv"
}
```

---

### GET /price/history/range

**Description**: Gets the lowest and highest price in a time range

**Query Parameters**:
- `token` (required): The token address
- `time_from` (required): Start time (unix timestamp)
- `time_to` (required): End time (unix timestamp)

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"token": "HEZ6KcNNUKaWvUCBEe4BtfoeDHEHPkCHY9JaDNqrpump",
"price": {
"lowest": {
"price": 0.000048405946337731886,
"time": 1740009112
},
"highest": {
"price": 0.003417425506087095,
"time": 1740216420
}
}
}
```

---

### POST /price

**Pagination**: Supported (cursor-based)

---

### GET /price/multi

**Description**: Gets price information for multiple tokens (up to 100).

**Pagination**: Supported (cursor-based)

**Notes**:
- Batch endpoint for multiple items

---

### POST /price/multi

**Pagination**: Supported (cursor-based)

**Notes**:
- Batch endpoint for multiple items

---

## Wallet Endpoints

### GET /wallet/{owner}

**Description**: Gets all tokens in a wallet with current value in USD.

**Path Parameters**:
- `owner` (required): The owner identifier

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"tokens": [
{
"token": {
"name": "Wrapped SOL",
"symbol": "SOL",
"mint": "So11111111111111111111111111111111111111112",
"uri": "",
"decimals": 9,
"image": "https://image.solanatracker.io/proxy?url=https%3A%2F%2Fcoin-images.coingecko.com%2Fcoins%2Fimages%2F21629%2Flarge%2Fsolana.jpg%3F1696520989",
"hasFileMetaData": true,
"creation": {
"creator": "9zGpUxJr2jnkwSSF9VGezy6aALEfxysE19hvcRSkbn15",
"created_tx": "5eHbuGuF1GfFcBgHcym69A1ErUYzY5vD2tE5hJ4A71yvZ7U3e93xMy1CWeH1HcAiyy6Yi8GDoJjeSXHhuDC4CFnW",
"created_time": 1749298225
}
},
"pools": [...],
"events": {...},
"risk": {...},
"balance": 0.775167121,
"value": 112.31297732160377
}
"total": 228.41656975961473,
"totalSol": 1.5750283296373857,
"timestamp": "2024-08-15 12:49:06"
}
```

---

### GET /wallet/{owner}/basic

**Description**: Gets all tokens in a wallet with current value in USD (lightweight, non-cached option).

**Path Parameters**:
- `owner` (required): The owner identifier

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"tokens": [
{
"address": "So11111111111111111111111111111111111111112",
"balance": 0.019911506,
"value": 2.4810073805356456,
"price": {
"quote": 1,
"usd": 124.60169414285619
},
"marketCap": {
"quote": 79833267.86038868,
"usd": 9953124295.82677
},
"liquidity": {
"quote": 395459.208121804,
"usd": 49303439.00300889
}
},
{
"address": "9BT13kNGQFKvSj2BibHPKmpxxSnqMFUEEZEMQ5SNpump",
"balance": 35145.6526,
"value": 0.07660938412685546,
"price": {
"usd": 0.0000021797684339159336,
"quote": 1.6913819975765577e-8
},
"marketCap": {
"usd": 2178.6061946025698,
"quote": 16.904801629500383
},
"liquidity": {
"usd": 4300.296098435483,
"quote": 33.367963734
}
},
{
"address": "EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm",
"balance": 0.078177,
"value": 0.03318780628945246,
"price": {
"usd": 0.42452135908838234,
"quote": 0.0034070271837690056
},
"marketCap": {
"usd": 424029286.2902132,
"quote": 3403078.017575447
},
"liquidity": {
"usd": 7978691.886756113,
"quote": 64033.57467683
}
},
{
"address": "AF7CYuqRw61atGBVT9LpxaXuSW9RuGmfnSAEgaHppump",
"balance": 2143.21592,
"value": 0.0075007010716513205,
"price": {
"usd": 0.0000034997412074334164,
"quote": 2.7995661589662763e-8
},
"marketCap": {
"usd": 3499.7412074334165,
"quote": 27.995661589662763
},
"liquidity": {
"usd": 7505.524527654956,
"quote": 60.039332132
}
}
"total": 2.598305272023605,
"totalSol": 0.02085288879816225
}
```

---

### GET /wallet/{owner}/page/{page}

**Description**: Retrieves wallet tokens using pagination with a limit of 250 tokens per request.

**Path Parameters**:
- `owner` (required): The owner identifier
- `page` (required): The page identifier

**Pagination**: Supported (cursor-based)

---

### GET /wallet/{owner}/trades

**Description**: Gets the latest trades of a wallet.

**Path Parameters**:
- `owner` (required): The owner identifier

**Query Parameters**:
- `page` (optional): Page number for pagination
- `limit` (optional): Number of trades per page

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"trades": [
{
"tx": "Transaction Signature here",
"from": {
"address": "So11111111111111111111111111111111111111112",
"amount": 0.00009999999747378752,
"token": {
"name": "Wrapped SOL",
"symbol": "SOL",
"image": "https://image.solanatracker.io/proxy?url=https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/So11111111111111111111111111111111111111112/logo.png",
"decimals": 9
}
},
"to": {
"address": "4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R",
"amount": 0.00815899996086955,
"token": {
"name": "Raydium",
"symbol": "RAY",
"image": "https://image.solanatracker.io/proxy?url=https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R/logo.png",
"decimals": 6
}
},
"price": {
"usd": 1.7136074522202307,
"sol": ""
},
"volume": {
"usd": 0.014018403988365319,
"sol": 0.00009999999747378752
},
"wallet": "WALLET_ADDRESS",
"program": "raydium",
"time": 1722759119596
}
"nextCursor": 1722759119596,
"hasNextPage": true
}
```

---

### GET /wallet/{owner}/chart

**Description**: Gets wallet portfolio chart data with historical values and PnL information.

**Path Parameters**:
- `owner` (required): The owner identifier

**Pagination**: Supported (cursor-based)

**Notes**:
- OHLCV data endpoint with customizable time intervals

**Response Example**:
```json
{
"chartData": [
{
"date": "2024-12-08",
"value": 890670.2,
"timestamp": 1733692405000,
"pnlPercentage": 0
},
{
"date": "2024-05-14",
"value": 1450.27,
"timestamp": 1715668377000,
"pnlPercentage": -99.84
},
{
"date": "2025-01-22",
"value": 3938345.2,
"timestamp": 1737554275000,
"pnlPercentage": 575.17
}
"pnl": {
"24h": {
"value": 105528.2,
"percentage": 2.8
},
"30d": {
"value": 3346283.26,
"percentage": 634.99
}
}
}```
```

---

## Trade Endpoints

### GET /trades/{tokenAddress}/{poolAddress}

**Description**: Gets the latest trades for a specific token and pool pair.

**Path Parameters**:
- `tokenAddress` (required): The tokenAddress identifier
- `poolAddress` (required): The poolAddress identifier

**Query Parameters**:
- `page` (optional): Page number for pagination
- `limit` (optional): Number of trades per page

**Pagination**: Supported (cursor-based)

---

### GET /trades/{tokenAddress}/{poolAddress}/{owner}

**Description**: Gets the latest trades for a specific token, pool, and wallet address.

**Path Parameters**:
- `tokenAddress` (required): The tokenAddress identifier
- `poolAddress` (required): The poolAddress identifier
- `owner` (required): The owner identifier

**Pagination**: Supported (cursor-based)

---

### GET /trades/{tokenAddress}/by-wallet/{owner}

**Path Parameters**:
- `tokenAddress` (required): The tokenAddress identifier
- `owner` (required): The owner identifier

**Pagination**: Supported (cursor-based)

---

## Chart Data Endpoints

### GET /chart/{token}

**Description**: Gets OHLCV (Open, High, Low, Close, Volume) data for charts.

**Path Parameters**:
- `token` (required): The token identifier

**Query Parameters**:
- `type` (optional): Time interval (e.g., '1s', '1m', '1h', '1d')
- `time_from` (optional): Start time (Unix timestamp in seconds)
- `time_to` (optional): End time (Unix timestamp in seconds)
- `marketCap` (optional): Return chart for market cap instead of pricing
- `removeOutliers` (optional): Set to false to disable outlier removal, true by default

**Available Intervals**: `1s`, `1h`, `5s`, `2h`, `15s`, `4h`, `1m`, `6h`, `3m`, `8h`, `5m`, `12h`, `15m`, `1d`, `30m`, `3d`, `1w`, `1mn`

**Note**: `1m` = 1 minute, `1mn` = 1 month

**Pagination**: Supported (cursor-based)

**Notes**:
- OHLCV data endpoint with customizable time intervals

**Response Example**:
```json
{
"oclhv": [
{
"open": 0.011223689525154462,
"close": 0.011223689525154462,
"low": 0.011223689525154462,
"high": 0.011223689525154462,
"volume": 683.184501136,
"time": 1722514489
},
{
"open": 0.011223689525154462,
"close": 0.011257053686384555,
"low": 0.011257053686384555,
"high": 0.011257053686384555,
"volume": 12788.70421942799,
"time": 1722514771
}
]
}
```

---

### GET /chart/{token}/{pool}

**Description**: Gets OHLCV (Open, High, Low, Close, Volume) data for charts.

**Path Parameters**:
- `token` (required): The token identifier
- `pool` (required): The pool identifier

**Query Parameters**:
- `type` (optional): Time interval (e.g., '1s', '1m', '1h', '1d')
- `time_from` (optional): Start time (Unix timestamp in seconds)
- `time_to` (optional): End time (Unix timestamp in seconds)
- `marketCap` (optional): Return chart for market cap instead of pricing
- `removeOutliers` (optional): Set to false to disable outlier removal, true by default

**Available Intervals**: `1s`, `1h`, `5s`, `2h`, `15s`, `4h`, `1m`, `6h`, `3m`, `8h`, `5m`, `12h`, `15m`, `1d`, `30m`, `3d`, `1w`, `1mn`

**Note**: `1m` = 1 minute, `1mn` = 1 month

**Pagination**: Supported (cursor-based)

**Notes**:
- OHLCV data endpoint with customizable time intervals

**Response Example**:
```json
{
"oclhv": [
{
"open": 0.011223689525154462,
"close": 0.011223689525154462,
"low": 0.011223689525154462,
"high": 0.011223689525154462,
"volume": 683.184501136,
"time": 1722514489
},
{
"open": 0.011223689525154462,
"close": 0.011257053686384555,
"low": 0.011257053686384555,
"high": 0.011257053686384555,
"volume": 12788.70421942799,
"time": 1722514771
}
]
}
```

---

### GET /holders/chart/{token}

**Description**: Gets token holder count data over time. Returns up to 1000 of the most recent data points.

**Path Parameters**:
- `token` (required): The token identifier

**Pagination**: Supported (cursor-based)

**Notes**:
- OHLCV data endpoint with customizable time intervals

**Response Example**:
```json
{
"holders": [
{
"holders": 1235,
"time": 1722414489
},
{
"holders": 1242,
"time": 1722514771
}
]
}
```

---

## PnL Data Endpoints

### GET /pnl/{wallet}

**Description**: Gets Profit and Loss data for all positions of a wallet.

**Path Parameters**:
- `wallet` (required): The wallet identifier

**Pagination**: Supported (cursor-based)

**Notes**:
- Profit and Loss calculation endpoint

**Response Example**:
```json
{
"tokens": {
"85tgA28eJCUwpTGkREdocDtkHCgZZySyrdv35w6opump": {
"holding": 34909.416624,
"held": 402288.62697,
"sold": 367379.210346,
"realized": 48.24649003,
"unrealized": 4665.26723313,
"total": 4713.51372317,
"total_sold": 1195.95048046,
"total_invested": 1256.76208526,
"average_buy_amount": 38.08369955,
"current_value": 4774.3253279697965,
"cost_basis": 0.00312403
}
},
"summary": {
"realized": 2418.42956164,
"unrealized": -634.74038817,
"total": 1783.68917347,
"totalInvested": 103020.70911717,
"averageBuyAmount": 1535.12073025,
"totalWins": 222,
"totalLosses": 295,
"winPercentage": 34.8,
"lossPercentage": 46.24
}
}
```

---

### GET /first-buyers/{token}

**Path Parameters**:
- `token` (required): The token identifier

**Query Parameters**:
- `limit` (optional): Number of first buyers to return

**Pagination**: Supported (cursor-based)

---

### GET /pnl/{wallet}/{token}

**Description**: Gets Profit and Loss data for a specific token in a wallet.

**Path Parameters**:
- `wallet` (required): The wallet identifier
- `token` (required): The token identifier

**Pagination**: Supported (cursor-based)

**Notes**:
- Profit and Loss calculation endpoint

**Response Example**:
```json
{
"holding": 0,
"held": 51095238.095238,
"sold": 51095238.095238,
"sold_usd": 776.90009082,
"realized": 588.64143114,
"unrealized": 0,
"total": 588.64143114,
"total_sold": 776.90009082,
"total_invested": 188.25865968,
"average_buy_amount": 188.25865968,
"current_value": 0,
"cost_basis": 0.00000368,
"first_buy_time": 1743274275720,
"last_buy_time": 1743274275720,
"last_sell_time": 1743274299334,
"last_trade_time": 1743274299334,
"buy_transactions": 1,
"sell_transactions": 1,
"total_transactions": 2
}
```

---

## Top Traders Endpoints

### GET /top-traders/all

**Pagination**: Supported (cursor-based)

---

### GET /top-traders/all/{page}

**Path Parameters**:
- `page` (required): The page identifier

**Pagination**: Supported (cursor-based)

---

### GET /top-traders/{token}

**Path Parameters**:
- `token` (required): The token identifier

**Pagination**: Supported (cursor-based)

---

## Stats and Events Endpoints

### GET /stats/{token}

**Description**: Gets detailed stats for a token or token-pool pair over various time intervals.

**Path Parameters**:
- `token` (required): The token identifier

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"1m": {
"buyers": 7,
"sellers": 9,
"volume": {
"buys": 642.307406481682,
"sells": 3071.093119714688,
"total": 3713.4005261963716
},
"transactions": 102,
"buys": 90,
"sells": 12,
"wallets": 14,
"price": 0.0026899499819631667,
"priceChangePercentage": 0.017543536395684036
},
"5m": {...},
"15m": {...},
"24h": {...}
}
```

---

### GET /stats/{token}/{pool}

**Description**: Gets detailed stats for a token or token-pool pair over various time intervals.

**Path Parameters**:
- `token` (required): The token identifier
- `pool` (required): The pool identifier

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"1m": {
"buyers": 7,
"sellers": 9,
"volume": {
"buys": 642.307406481682,
"sells": 3071.093119714688,
"total": 3713.4005261963716
},
"transactions": 102,
"buys": 90,
"sells": 12,
"wallets": 14,
"price": 0.0026899499819631667,
"priceChangePercentage": 0.017543536395684036
},
"5m": {...},
"15m": {...},
"24h": {...}
}
```

---

### GET /events/{tokenAddress}

**Description**: Gets raw event data for live processing. Returns binary data that needs to be decoded.

**Path Parameters**:
- `tokenAddress` (required): The tokenAddress identifier

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"wallet": "8psNvWTrdNTiVRNzAgsou9kETXNJm2SXZyaKuJraVRtf",
"amount": 5.677347,
"priceUsd": 10.472407812562192,
"volume": 59.455493077426524,
"type": "sell",
"time": 1749298583015
},
{
"wallet": "7ACsEkYSvVyCE5AuYC6hP1bNs4SpgCDwsfm3UdnyPERk",
"amount": 2469629.599217,
"priceUsd": 0.0000098468505465602,
"volume": 245.0468505465602,
"type": "buy",
"time": 1749298314879
}
]
```

---

### GET /events/{tokenAddress}/{poolAddress}

**Description**: Gets raw event data for a specific token and pool. Returns binary data that needs to be decoded.

**Path Parameters**:
- `tokenAddress` (required): The tokenAddress identifier
- `poolAddress` (required): The poolAddress identifier

**Pagination**: Supported (cursor-based)

---

## Credits Endpoints

### GET /credits

**Description**: Gets the remaining API credits for your API key.

**Pagination**: Supported (cursor-based)

**Response Example**:
```json
{
"credits": 9976168
}
```

---

