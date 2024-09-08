OG_DIR="/Users/francis/GitHub/fmadarang-react/website/build/static"
TGT_DIR="/Users/francis/GitHub/fmadarang.com/main/pages/static"
INDEX_FILE="/Users/francis/GitHub/fmadarang-react/website/build/index.html"
INDEX_CP="/Users/francis/GitHub/fmadarang.com/main/pages/templates/index.html"
replace_homepage() {
    rm -r $TGT_DIR/css
    rm -r $TGT_DIR/js
    rm -r $TGT_DIR/media
    cp -r $OG_DIR/css $TGT_DIR/
    cp -r $OG_DIR/js $TGT_DIR/
    cp -r $OG_DIR/media $TGT_DIR/
    cp $INDEX_FILE $INDEX_CP
}