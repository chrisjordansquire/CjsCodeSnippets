
use strict;
use warnings;
use diagnostics;

my $upper = $ARGV[0];
if( not $upper ){
    $upper = 4000000;
}

my $sum =0;

my $n1 = 1;
my $n2 = 2;
while( $n2 < $upper ){
    if( $n2 % 2 == 0){
        $sum += $n2;
    }
    $n2 = $n1 + $n2;
    $n1 = $n2 - $n1;

}

print "The sum of all fibonacci numbers less than $upper is $sum\n"
