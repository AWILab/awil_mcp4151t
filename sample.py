import time
import math

from awil_ft232h import AwilFt232h
from awil_mcp4151t import MCP4151

# SPI設定
supply_voltage = 3.3
spi_channel = 2
spi_frequency = 1E6

# AwilFt232hインスタンスを初期化
ft232h = AwilFt232h()
ft232h.open("ADCSPI02_002")

# MCP4151インスタンスの初期化
mcp4151 = MCP4151(ft232h, spi_channel, spi_frequency)

# ワイパーの値を0〜255の範囲で変化させる例
count = 0
start_time = time.time()
while count < 256:
    mcp4151.set_wiper(count)  # ワイパー値を設定
    print(f"Set wiper value to: {count}")
    time.sleep(0.01)  # 少し待機
    count += 1

end_time = time.time()
print("Total time (sec): ", (end_time - start_time))

# 通信を終了
ft232h.close()
