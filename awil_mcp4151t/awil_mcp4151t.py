from typing import List
from awil_ft232h import AwilFt232h

# データシート
# https://ww1.microchip.com/downloads/en/devicedoc/22060b.pdf

class AwilMcp4151:
    def __init__(self, awil_ft232h: AwilFt232h, spi_channel=0, max_speed_hz=1000000):
        """
        MCP4151クラスの初期化
        awil_ft232h: AwilFt232hクラスのインスタンス
        spi_channel: 使用するSPIチャンネル
        max_speed_hz: SPI通信の最大速度
        """
        self._awil_ft232h = awil_ft232h
        self._spi_channel = spi_channel
        self._max_speed_hz = max_speed_hz

    def set_wiper(self, value):
        """
        MCP4151のワイパー値を設定します。
        value: 0〜255の範囲でワイパー値を設定
        """
        if not 0 <= value <= 255:
            raise ValueError("ワイパー値は0〜255の範囲で指定してください。")

        command = [0x00, value]  # コマンドとワイパー値を送信するデータ
        self._awil_ft232h.exchange(command, self._spi_channel, self._max_speed_hz, spi_mode=0b00)

    def close(self):
        """
        FT232Hとの通信を終了します。
        """
        self._awil_ft232h.close()