if (-1 || 0) alert( 'first' ); // executes
if (-1 && 0) alert( 'second' );
if (null || -1 && 1) alert( 'third' ); // executes
// Solution : (-1 || 0 ) values are both truthy , -1
// (-1 && 0 ) -> 0 is falsy
// null || -1 && 1 -> null || 1 -> 1
