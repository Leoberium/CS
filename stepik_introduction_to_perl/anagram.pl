#!/usr/bin/perl
use strict;
use warnings;
use utf8;
use v5.22;
use Data::Dumper;

sub anagram {
    my $array_ref = shift;
    my (%all, %uniq);
    for (grep { !$uniq{$_}++ } map lc, @$array_ref) {
        push @{$all{join '', sort( split //, $_ )}}, $_;
    }
    return { map { $_->[0] => $_ } grep { scalar @{$_} > 1 } values %all };
}

my $result = anagram(['пятак', 'ЛиСток', 'пятка', 'стул', 'ПяТаК', 'слиток', 'тяпка', 'столик', 'слиток']);
say "$_: @{$result->{$_}}" for sort keys %$result;