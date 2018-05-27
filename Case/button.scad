/*
@file: button.scad

Copyright (C) 2018 by Alejandro Vicario and the IllBee contributors.

This file is part of the IllBee project.

IllBee is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

IllBee is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with IllBee.  If not, see <http://www.gnu.org/licenses/>.
*/

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
