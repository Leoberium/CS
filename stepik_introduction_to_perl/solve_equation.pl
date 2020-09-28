#!/usr/bin/perl
use warnings;
use strict;

sub solve_equation {
    my ($a_value, $b_value, $c_value) = @_;
    my ($x1, $x2);
    my $d = $b_value**2 - 4 * $a_value * $c_value;
    if ($a_value == 0 || $d < 0) {print "No solution!\n";}
    elsif ($d == 0) {
        $x1 = -$b_value / (2 * $a_value);
        print "$x1\n";
    }
    else {
        $x1 = (-$b_value - $d**0.5) / (2 * $a_value);
        $x2 = (-$b_value + $d**0.5) / (2 * $a_value);
        if ($x1 < $x2) {print "$x1, $x2\n";}
        else {print "$x2, $x1\n"}
    }
}

while (my $line = <>) {
    solve_equation(split / /, $line);
}