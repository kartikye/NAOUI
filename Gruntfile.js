module.exports = function(grunt) {

    // 1. All configuration goes here 
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        //concat: {   
        //    dist: {
        //        src: [
        //            'assets/scripts/**/**/*.js'
        //        ],
        //        dest: 'assets/scripts/production.js',
        //    }
        //},

        //uglify: {
        //    build: {
        //        src: 'assets/scripts/scripts.js',
        //        dest: 'assets/scripts/scripts.min.js'
        //    }
        //},*/

        sass: {
	    dist: {
	        options: {
		    style: 'nested'
		},
		files: [{
		    expand: true,
		    cwd: 'assets/styles/scss',
		    src: ['*.scss'],
		    dest: 'assets/styles/css',
		    ext: '.css'
		}]
	    }
	},

	coffee: {
       	    build: {
		expand: true,
		flatten: true,
	        cwd: 'assets/scripts/',
	        src: ['libs/*.coffee'],
	        dest: 'assets/scripts/libs',
	        ext: '.js'
	    }
	},

	watch: {
	    options: {
		livereload: true
	    },

	    coffee: {
		files: ['assets/scripts/**/*.coffee'],
		tasks: ['coffee'],
		options: {
		    spawn: false,
		}
	    },

            scripts: {
                files: ['assets/scripts/**/*.js'],
                tasks: ['concat'],
                options: {
                    spawn: false,
                }
            },

	    css: {
		files: ['assets/styles/scss/*.scss'],
		tasks: ['sass'],
		options: {
		    spawn: false
		}
	    }
        }

    });

    // 3. Where we tell Grunt we plan to use this plug-in.
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-coffee');

    // 4. Where we tell Grunt what to do when we type "grunt" into the terminal.
    grunt.registerTask('default', ['coffee', 'sass', 'watch']);

};
