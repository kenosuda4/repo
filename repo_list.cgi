#!C:\Strawberry/perl/bin/perl

use strict;
use warnings;
	
#cgiヘッダーの出力
print "Content-Type: text/html;charset=utf-8\n\n";

open(FILE, "repo.html");
my @html = <FILE>;
close(FILE);

for my $html (@html){
	print $html;
}

exit;