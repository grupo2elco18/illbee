dia = 10;
height_top = 5;
support_offset = 1;
support_heigth = 9;
support_length = 2;
support_width = 1.5;
hole = [4.5, 2.3];
hole_deep = 4;
wall_thickness = 2;

/******************************************************************************/

$fn = 50;
height = height_top + wall_thickness + support_heigth;
support_size = dia + support_offset*2;

/******************************************************************************/


difference() {
	union() {
		cylinder(d=dia, h=height);

		translate([0, 0, -support_length/2+support_heigth-wall_thickness]) {
			hull() {
				cube(size=[support_size, support_width, support_length], center=true);
				cube(size=[support_width, support_size, support_length], center=true);
				translate([0, 0, -support_length/2]) {
					cylinder(d=dia, h=support_length*2, center=true);
				}
			}
		}
	}

	rotate([0, 0, 45]) translate([-hole[0]/2, -hole[1]/2, -1]) {
		cube(size=[hole[0], hole[1], hole_deep+1]);
	}
}
