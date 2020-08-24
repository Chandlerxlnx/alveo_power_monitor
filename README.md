### alveo_card_pwr_gather
### this script is to recoder realtime working power of the ALVEO U200 card
#### It is depend on
####  1 ALVEO U200
####  2 xilinx_u200_xdma_201830_2 shell 
#### 3 XRT 2019.1
  
### Userage:
#> python pwr.py <file_name(.csv)> <interval(s)> <counter(int)>
### Example:
#> python pwr.py pwr.csv 15 100
按照15秒一个点采集100个点 card0 和card1 的瞬时功耗

