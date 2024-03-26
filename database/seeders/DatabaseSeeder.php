<?php

namespace Database\Seeders;

use App\Models\User;
// use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     */
    public function run(): void
    { // https://fakerphp.github.io/
        $this->call([
            UserSeeder::class,
            SubscriberSeeder::class,
            NewsletterSeeder::class,
            RecipeSeeder::class,
            TagSeeder::class,
            RecipeTagAssignmentSeeder::class,
            CommentSeeder::class,
        ]);
    }
}
