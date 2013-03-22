set terminal pngcairo size 400,400 enhanced font 'Verdana,10'
set output 'bars.png'

set style data histogram

set ylabel "% av fokustid"
set yrange [0:2]

set style fill solid border rgb "black"

#plot 'contact-result.txt' every ::1::1 using 2:xtic(1)
plot 'contact-result.txt' every ::0::0 using 1:xtic('') title 'Monsterkontakt', 'nocontact-result.txt' every ::0::0 using 1:xtic('') title 'Ingen Monsterkontakt'