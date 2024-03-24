<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Subscriber;

class SubscriberSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        for($i = 0; $i < 1000; $i++){
            Subscriber::updateOrCreate([
                'email' => fake()->safeemail,                
            ],
            [
                'name' => fake()->name,
                'email' => fake()->email
            ]
        );
        }
    }
}
