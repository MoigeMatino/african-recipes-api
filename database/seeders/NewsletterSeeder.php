<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Newsletter;

class NewsletterSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        for($i=0; $i<20; $i++) {
            $newsletter = new Newsletter();
            $newsletter->title = fake()->sentence;
            $newsletter->content = fake()->randomHtml;
            $newsletter->status = fake()->randomElement(['draft', 'published']);
            $newsletter->save();
        }
    }
}
