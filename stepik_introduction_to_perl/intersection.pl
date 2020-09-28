#!/usr/bin/perl
use strict;
use warnings;

sub intersection {
    my ($set1, $set2) = @_;
    my %hash = map { $_ => 1 } grep { exists $set1->{$_} } %$set2;
    return \%hash;
}

my $set1 = {a => 1, b => 1, c => 1};
my $set2 = {b => 1, c => 1, d => 1};
print join ', ', intersection($set1, $set2);
