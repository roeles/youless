epoch_diff=946684800
t0e = t0 - epoch_diff
t1e = t1 - epoch_diff

set key left top

set xrange [t0-epoch_diff:t1-epoch_diff]
set xdata time
set timefmt "%s"
set format x "%d-%m %H:%M"
set ylabel "Power (watt)"
set title "Power usage"
set logscale y
set autoscale y
#set yrange [0:1000]
plot "./watt.csv" using 1:2 with lines notitle

