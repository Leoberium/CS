#!/usr/bin/perl
use strict;
use warnings;

require "./product.pm";

my $product = Local::Product->new(name => 'Фуфырка обыкновенная', price_rur => 350, count => 5);
print $product->price_rur, "\n";
print $product->price_usd, "\n";

$product->price_usd(7);
print $product->price_rur, "\n";
print $product->price_usd, "\n";

$product->count(10);
print $product->sum_rur, "\n";
print $product->sum_usd, "\n";