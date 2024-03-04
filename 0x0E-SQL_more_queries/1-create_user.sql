-- This script creates the MySQL server user user_0d_1 if it doesn't already exist.

-- Check if the user exists
SELECT user FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost' INTO @user_exists;

-- If the user does not exist, create it
IF @user_exists IS NULL THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
ELSE
	GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
END IF;
