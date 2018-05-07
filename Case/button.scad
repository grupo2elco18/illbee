dia = 10;
height = 10;
support_offset = 1;
support_heigth = 5;
support_width = 1.5;
hole = [2, 1];
hole_deep = 5;

/******************************************************************************/

$fn = 50;
support_size = dia + support_offset*2;

/******************************************************************************/

difference() {
	union() {
		cylinder(d=dia, h=height);

		translate([0, 0, support_heigth/2]) {
			cube(size=[support_size, support_width, support_heigth], center=true);
		}

		translate([0, 0, support_heigth/2]) {
			cube(size=[support_width, support_size, support_heigth], center=true);
		}
	}

	translate([-hole[0]/2, -hole[1]/2, -1]) {
		cube(size=[hole[0], hole[1], hole_deep+1]);
	}
}
