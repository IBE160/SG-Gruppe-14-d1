-- Create the profiles table
CREATE TABLE profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id),
    name TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Add a comment to the table
COMMENT ON TABLE profiles IS 'Stores public user profile information.';
