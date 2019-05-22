/* Copyright (C) 2006 Peter Selinger. This file is distributed under
   the terms of the GNU General Public License. See the file COPYING
   for details. */

#include <stdio.h>

/* do something innocent */
int main_good(int ac, char *av[]) {
  fprintf(stdout, "md5 is insecure\n");
  fflush(stdout);
  return 0;
}

/* do something evil */
int main_evil(int ac, char *av[]) {
  fprintf(stdout, "sha1 is insecure too");
  fflush(stdout);
  return 0;
}
