'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass')(require('sass'));
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');

// compile scss to css
gulp.task('sass-wedding', function () {
    return gulp.src('./sass-wedding/styles.scss')
        .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
        .pipe(rename({basename: 'styles.min'}))
        .pipe(gulp.dest('./css-wedding'));
});

// watch changes in scss files and run sass task
gulp.task('sass-wedding:watch', function () {
    gulp.watch('./sass-wedding/**/*.scss', ['sass-wedding']);
});

// minify js
gulp.task('minify-js', function () {
    return gulp.src('./js-wedding/scripts.js')
        .pipe(uglify())
        .pipe(rename({basename: 'scripts.min'}))
        .pipe(gulp.dest('./js-wedding'));
});

// default task
gulp.task('default', gulp.series('sass-wedding', 'minify-js'));