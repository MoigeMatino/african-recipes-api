<?php

namespace Database\Seeders;

use App\Models\Recipe;
use App\Models\User;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class RecipeSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $users = User::all()->pluck("id")->toArray();

        foreach ($users as $user_id) {
            Recipe::create([
                'user_id' => $user_id,
                'title' => fake()->sentence,
                'description' => fake()->paragraph,
                'instructions' => fake()->randomHtml,
                'prep_time' => fake()->text,
                'cook_time' => fake()->sentence(2),
                'total_time' => fake()->sentence(2),
                'servings' => fake()->randomDigit,
                'image_url' => fake()->imageUrl(640, 480, 'animals', true),
                'premium' => fake()->randomElement([true, false]),
                'ingredients' => json_encode(array_fill(0, 3, [
                    'name' => fake()->sentence,
                    'amount' => fake()->randomNumber(2, false),
                    'unit' => fake()->randomElement(['g', 'kg', 'ml', 'l', 'cup', 'piece']),
                ])),
                'nutritional_info' => json_encode([
                    'calories' => fake()->randomFloat(2, 0, 1000),
                   'saturated_fat' => fake()->randomFloat(2, 0, 1000)
                   'carbohydrates' => fake()->randomFloat(2,1,1000),
                   'protein' => fake()->randomFloat(2,1,1000)
                
                ]),
        ]);
        };
    }
}
