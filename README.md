# XUID to UUID 轉換器

一個幫助 Minecraft Java 版伺服器管理員將基岩版（Bedrock）玩家加入白名單的工具。

## 功能說明

這個工具可以將 Xbox Gamertag 轉換為 UUID 格式，讓 Minecraft Java 版伺服器管理員能夠將基岩版玩家添加到白名單中。

### 為什麼需要這個工具？

Minecraft 基岩版玩家使用的是 XUID (Xbox User ID) 而不是標準的 UUID 格式。當你想在 Minecraft Java 版伺服器的白名單中添加基岩版玩家時，需要將他們的 XUID 轉換為特定的 UUID 格式。

## 使用方法

### 安裝依賴

```bash
pip install requests
```

### 運行程式

```bash
python3 xuid_to_uuid.py "玩家的Gamertag"
```

### 輸出示例

```bash
$ python3 xuid_to_uuid.py "testplayer"
{
  "uuid": "00000000-0000-0000-0009-0000001F8896",
  "name": ".testplayer"
}
```

## 將玩家加入白名單

獲取到 UUID 後，你可以將玩家添加到 Minecraft 伺服器的白名單中：

### 方法一：使用伺服器指令

1. 進入伺服器控制台或使用 `/minecraft` 指令
2. 輸入：`/whitelist add <UUID>`

### 方法二：編輯 whitelist.json

1. 打開伺服器目錄下的 `whitelist.json` 檔案
2. 添加以下內容：

```json
{
  "uuid": "00000000-0000-0000-0009-0000001F8896",
  "name": ".testplayer"
}
```

3. 儲存檔案並重新載入伺服器：`/whitelist reload`

## API 說明

本工具使用 [GeyserMC API](https://api.geysermc.org/v2/xbox/xuid/{gamertag}) 來查詢 Xbox Gamertag 對應的 XUID。

## 限制

- 只能查詢已存在的 Xbox Gamertag
- 查詢頻率請適度，避免對 API 造成過大負擔

## 授權條款

MIT License

---

# XUID to UUID Converter

A tool to help Minecraft Java Edition server administrators whitelist Bedrock Edition players.

## Features

This tool converts Xbox Gamertags to UUID format, allowing Minecraft Java Edition server administrators to add Bedrock players to their whitelist.

## Why do you need this tool?

Minecraft Bedrock Edition players use XUID (Xbox User ID) instead of standard UUID format. When you want to add a Bedrock player to your Minecraft Java Edition server's whitelist, you need to convert their XUID to a specific UUID format.

## Usage

### Install Dependencies

```bash
pip install requests
```

### Run the Program

```bash
python3 xuid_to_uuid.py "Gamertag"
```

### Example Output

```bash
$ python3 xuid_to_uuid.py "testplayer"
{
  "uuid": "00000000-0000-0000-0009-0000001F8896",
  "name": ".testplayer"
}

```

## Adding Players to Whitelist

After obtaining the UUID, you can add the player to your Minecraft server's whitelist:

### Method 1: Using Server Commands

1. Enter the server console or use `/minecraft` command
2. Type: `/whitelist add <UUID>`

### Method 2: Edit whitelist.json

1. Open the `whitelist.json` file in your server directory
2. Add the following content:

```json
{
  "uuid": "00000000-0000-0000-0009-0000001F8896",
  "name": ".testplayer"
}
```

3. Save the file and reload the server: `/whitelist reload`

## API Information

This tool uses the [GeyserMC API](https://api.geysermc.org/v2/xbox/xuid/{gamertag}) to query the XUID corresponding to an Xbox Gamertag.

## Limitations

- Can only query existing Xbox Gamertags
- Please use moderately and avoid overloading the API

## License

MIT License
