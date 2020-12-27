package module;{
    sub STDIN{[
        my $PostData = "";
        read (STDIN, $PostData, $ENV{'CONTENT_LENGTH'});
    }


}