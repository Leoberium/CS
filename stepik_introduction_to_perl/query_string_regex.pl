#!/usr/bin/perl
use strict;
use warnings;
use Data::Dumper;

sub parse_query_string {
    return { shift =~ /([^&=;]+)(?:=([^&=;]+))?/g }
}

print Dumper parse_query_string("key1=value1&key2=value2");