#!/usr/bin/perl
use strict;
use warnings;

$SIG{INT} = $SIG{TERM} = sub { exit };
# INT - Ctrl + C
# TERM - terminate signal

my $max_workers = shift || 5;
my $parent_id = "$$"; # process id


my @children;
for (1..$max_workers) {
    my $pid = fork;
    if (!defined $pid) {
        warn "failed to fork :$!";
        kill 'TERM', @children;
        exit;
    } elsif ($pid != 0) {
        push @children, $pid;
        next;
    }
    sleep 1;
    exit;
}
wait_children();

sub wait_children {
    while (scalar @children) {
        my $pid = $children[0];
        my $kid = waitpid $pid, 0;
        warn "Reaped $pid ($kid)\n";
        shift @children;
    }
}

END {
    if ($parent_id == $$) {
        wait_children();
    }
}