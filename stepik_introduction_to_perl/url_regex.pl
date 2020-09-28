#!/usr/bin/perl
use strict;
use warnings;
use Data::Dumper;

sub parse_url {
    my ($url) = @_;
    my $schema = '(?<schema>https?)';
    my $domain = '(?::\/{2}(?<domain>[^\s:\/\?#]+))';
    my $port = '(?::(?<port>\d+))?';
    my $path = '(?<path>[^\?#]+)?';
    my $query_string = '(?:\?(?<query_string>[^#]+))?';
    my $anchor = '(?:#(?<anchor>\w+))?';
    $url =~ qr/^$schema$domain$port$path$query_string$anchor$/;
    return %+;
}

my %res = parse_url("http://mail.ru:8080/r/p?s=10&z=11#text");
print Dumper \%res;