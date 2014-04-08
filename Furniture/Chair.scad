linear_extrude(height = 5) square([2]);
translate([3,0,0]) linear_extrude(height = 5) square([2]);
translate([3,3,0]) linear_extrude(height = 5) square([2]);
translate([0,3,0]) linear_extrude(height = 5) square([2]);

translate([-.5,-.5,5]) linear_extrude(height = 1) square(5);

translate([0,0,6]) linear_extrude(height = 5) square([1,4]);