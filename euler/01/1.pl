
use strict;
use warnings; 
use diagnostics;

my $sum = 0;
my $upper = $ARGV[0];
my $i;

if( not $upper ){
    $upper = 1000;
}

for(  $i = 0; $i<$upper; $i++){
    if( ($i % 3) == 0 || ($i % 5) == 0){
        $sum += $i;
    }
}

print "The total sum of multiples of 3 and 5 below $upper is $sum\n";
