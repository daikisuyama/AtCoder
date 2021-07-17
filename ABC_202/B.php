<?php
    echo str_replace("7","6",str_replace("6","9",str_replace("9","7",strrev(trim(fgets(STDIN))))));
?>