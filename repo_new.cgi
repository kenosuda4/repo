#!C:\Strawberry/perl/bin/perl -w

use strict;
use warnings;
use Smart::Comments;
#cgiヘッダーの出力

my $PostData = "";
my %IN = ();
read (STDIN, $PostData, $ENV{'CONTENT_LENGTH'});
foreach my $data (split(/&/, $PostData)) {
  (my $key, my $value) = split(/=/, $data);

  $IN{"$key"} = $value;
}
### %IN
my $DB = "./repo.csv";
open (DB, "> $DB");
print DB "$IN{id}, $IN{name}, $IN{repo}¥n";
close(DB);
# print() on closed filehandle 不明

print "Content-Type: text/html;charset=utf-8\n\n";

open(FILE, "repo_new.html");
my @html = <FILE>;
close(FILE);

for my $html (@html){
	print $html;
}

exit;