package Local::Product;
use strict;
use warnings;

sub new {
    my ($class, %args) = @_;
    my $n_args = grep { exists $args{$_} } qw/price_rur price_usd/;
    if ( $n_args != 1 || not exists $args{name} ) { return undef; }
    $n_args = grep { exists $args{$_} } qw/sum_rur sum_usd/;
    if ( $n_args != 0 ) { return undef; }
    $args{count} //= 1;
    return bless \%args, $class;
}

sub name {
    my $self = shift;
    $self->{name} = shift if @_;
    return $self->{name};
}

sub count {
    my $self = shift;
    if (@_) {
        $self->{count} = shift;
        $self->{sum_rur} = undef;
        $self->{sum_usd} = undef;
    }
    return $self->{count};
}

sub price_rur {
    my $self = shift;
    if (@_) {
        $self->{price_rur} = shift;
        $self->{price_usd} = undef;
        $self->{sum_rur} = undef;
        $self->{sum_usd} = undef;
    }
    $self->{price_rur} //= 70 * $self->{price_usd};
    return $self->{price_rur};
}

sub price_usd {
    my $self = shift;
    if (@_) {
        $self->{price_usd} = shift;
        $self->{price_rur} = undef;
        $self->{sum_rur} = undef;
        $self->{sum_usd} = undef;
    }
    $self->{price_usd} //= $self->{price_rur} / 70;
    return $self->{price_usd};
}

sub sum_rur {
    my $self = shift;
    $self->{sum_rur} //= $self->price_rur * $self->{count};
    return $self->{sum_rur};
}

sub sum_usd {
    my $self = shift;
    $self->{sum_usd} //= $self->price_usd * $self->{count};
    return $self->{sum_usd};
}

1;