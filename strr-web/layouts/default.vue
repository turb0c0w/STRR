<template>
    <div data-cy="default-layout">
        <div class="flex justify-between flex-col h-screen">
            <BcrosHeader></BcrosHeader>
                <div class="flex h-full justify-center">
                    <div class="w-[848px] py-[75px]">
                        <NuxtPage></NuxtPage>
                    </div> 
                </div>
            <BcrosFooter></BcrosFooter>
        </div>
    </div>
</template>
